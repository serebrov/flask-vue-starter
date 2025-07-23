<template>
  <div class="home">
    <h1>User Manager</h1>

    <div v-if="isLoading" class="loading">Loading...</div>

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
            <tr v-for="user in users" :key="user.id">
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
          <h3>{{ model.id ? `Edit User ID#${model.id}` : 'New User' }}</h3>
          <form @submit.prevent="saveUser">
            <div class="form-group">
              <label for="username">Username</label>
              <input
                type="text"
                id="username"
                v-model="model.username"
                placeholder="Enter username"
                required
              />
            </div>

            <div class="form-group">
              <label for="email">Email</label>
              <input
                type="email"
                id="email"
                v-model="model.email"
                placeholder="Enter email"
                required
              />
            </div>

            <button type="submit" class="btn btn-primary btn-full-width">Save User</button>
          </form>

          <div v-if="errors.length > 0" class="errors">
            <div v-for="error in errors" :key="error" class="error">
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
import { backend, type User, type UserCreateData } from '../backend'

const NO_USER: User = { id: '', username: '', email: '' }

const isLoading = ref(false)
const users = ref<User[]>([])
const model = ref<User>({ ...NO_USER })
const error = ref<any>(null)
const errors = ref<string[]>([])

onMounted(() => {
  refreshUsers()
})

async function refreshUsers() {
  isLoading.value = true
  try {
    const response = await backend.getUsers()
    users.value = response.data
  } catch (err) {
    parseError(err)
  }
  isLoading.value = false
}

function populateUserToEdit(user: User) {
  model.value = { ...user }
}

async function saveUser() {
  try {
    if (model.value.id) {
      await backend.updateUser(model.value.id, model.value as UserCreateData)
    } else {
      await backend.createUser(model.value as UserCreateData)
    }
    model.value = { ...NO_USER } // reset form
    await refreshUsers()
  } catch (err) {
    parseError(err)
  }
}

async function deleteUser(id: string) {
  if (confirm('Are you sure you want to delete this user?')) {
    // if we are editing a user we deleted, remove it from the form
    if (model.value.id === id) {
      model.value = { ...NO_USER }
    }
    await backend.deleteUser(id)
    await refreshUsers()
  }
}

function parseError(errorObj: any) {
  error.value = errorObj
  errors.value = []
  if (errorObj?.response?.data?.errors) {
    for (const [field, message] of Object.entries(
      errorObj.response.data.errors,
    )) {
      errors.value.push(`${field}: ${message}`)
    }
  } else if (errorObj?.message) {
    errors.value.push(errorObj.message)
  }
}
</script>

<style scoped>
.home {
  max-width: 100%;
}
</style>

