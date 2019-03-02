<template>
  <div>
    <div class="hero">
      <div>
        <h1 class="display-3">Hello World</h1>
        <p class="lead">The home</p>
      </div>
    </div>

    <div class="container-fluid mt-4">
      <h1 class="h1">User Manager</h1>
      <b-alert :show="isLoading" variant="info">Loading...</b-alert>
      <b-row>
        <b-col>
          <table class="table table-striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Email</th>
                <th>&nbsp;</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" :key="user.id">
                <td>{{ user.id }}</td>
                <td>{{ user.username }}</td>
                <td>{{ user.email }}</td>
                <td class="text-right">
                  <a href="#" @click.prevent="populateUserToEdit(user)">Edit</a> -
                  <a href="#" @click.prevent="deleteUser(user.id)">Delete</a>
                </td>
              </tr>
            </tbody>
          </table>
        </b-col>
        <b-col lg="3">
          <b-card :title="(model.id ? 'Edit User ID#' + model.id : 'New User')">
            <form @submit.prevent="saveUser">
              <b-form-group label="Username">
                <b-form-input type="text" v-model="model.username"></b-form-input>
              </b-form-group>
              <b-form-group label="Email">
                <b-form-textarea rows="4" v-model="model.email"></b-form-textarea>
              </b-form-group>
              <div>
                <b-btn type="submit" variant="success">Save User</b-btn>
              </div>
            </form>
          </b-card>
        </b-col>
        <b-col>
          {{ this.error }}
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import { backend, User } from '../backend'

const NO_USER = {'id': '', 'username': '', 'email': ''}

@Component({
})
export default class Home extends Vue {

  isLoading: Boolean = false
  users: Array<User> = []
  model: User = NO_USER
  error: Object = null

  async beforeMount() {
    this.refreshUsers()
  }

  async refreshUsers() {
    this.isLoading = true
    // this.users = await backend.getUsers()
    // this.isLoading = false

    backend.getUsers()
      .then(res => {
        this.users = res.data
      })
      .catch(err => {
        debugger;
        this.error = err
      })
      .then(() => {
        this.isLoading = false
      })
  }

  async populateUserToEdit(user) {
      this.model = Object.assign({}, user)
  }

  async saveUser() {
    try {
      if (this.model.id) {
        await backend.updateUser(this.model.id, this.model)
      } else {
        await backend.createUser(this.model)
      }
      this.model = NO_USER // reset form
      await this.refreshUsers()
    } catch(err) {
      this.error = err
    }
  }

  async deleteUser(id) {
    if (confirm('Are you sure you want to delete this user?')) {
      // if we are editing a users we deleted, remove it from the form
      if (this.model.id === id) {
        this.model = NO_USER
      }
      await backend.deleteUser(id)
      await this.refreshUsers()
    }
  }
}
</script>
