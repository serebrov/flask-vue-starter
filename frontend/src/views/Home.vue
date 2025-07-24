<template>
  <div class="home">
    <h1>User Manager</h1>

    <div v-if="userView.loading" class="loading">Loading...</div>

    <div class="content-grid">
      <div class="users-section">
        <table class="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Username</th>
              <th>Email</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in userView.users" :key="user.id">
              <td>{{ user.id }}</td>
              <td>{{ user.username }}</td>
              <td>{{ user.email }}</td>
              <td>
                <button @click="populateUserToEdit(user)" class="btn btn-info">
                  Edit
                </button>
                <button @click="deleteUser(user.id)" class="btn btn-danger">
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="form-section">
        <div class="card">
          <h3>{{ userView.getFormTitle() }}</h3>
          <form @submit.prevent="saveUser">
            <div class="form-group">
              <label for="username">Username</label>
              <input
                type="text"
                id="username"
                v-model="userView.currentUser.username"
                placeholder="Enter username"
                required
              />
            </div>

            <div class="form-group">
              <label for="email">Email</label>
              <input
                type="email"
                id="email"
                v-model="userView.currentUser.email"
                placeholder="Enter email"
                required
              />
            </div>

            <button type="submit" class="btn btn-primary btn-full-width">
              Save User
            </button>
          </form>

          <div v-if="userView.errors.length > 0" class="errors">
            <div v-for="error in userView.errors" :key="error" class="error">
              {{ error }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { UserView } from '../models/UserView'

const userView = ref(new UserView())

onMounted(() => {
  userView.value.refreshUsers()
})

function populateUserToEdit(user: any) {
  userView.value.setCurrentUser(user)
}

async function saveUser() {
  await userView.value.saveCurrentUser()
}

async function deleteUser(id: string) {
  await userView.value.deleteUserById(id)
}
</script>

<style scoped>
.home {
  max-width: 100%;
}
</style>
