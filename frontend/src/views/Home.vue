<template>
  <div>

    <div class="container mx-auto mt-4 px-4">
      <h1 class="text-3xl font-bold mb-4">User Manager</h1>
      
      <Message v-if="isLoading" severity="info" :closable="false">Loading...</Message>
      
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
        <div class="lg:col-span-3">
          <DataTable 
            :value="users" 
            :loading="isLoading"
            class="p-datatable-striped"
            responsiveLayout="scroll"
            :paginator="true"
            :rows="10"
          >
            <Column field="id" header="ID" sortable></Column>
            <Column field="username" header="Username" sortable></Column>
            <Column field="email" header="Email" sortable></Column>
            <Column header="Actions">
              <template #body="slotProps">
                <div class="flex gap-2">
                  <Button 
                    label="Edit" 
                    icon="pi pi-pencil" 
                    size="small"
                    @click="populateUserToEdit(slotProps.data)"
                  />
                  <Button 
                    label="Delete" 
                    icon="pi pi-trash" 
                    severity="danger" 
                    size="small"
                    @click="deleteUser(slotProps.data.id)"
                  />
                </div>
              </template>
            </Column>
          </DataTable>
        </div>
        
        <div class="lg:col-span-1">
          <Card>
            <template #title>
              {{ model.id ? `Edit User ID#${model.id}` : 'New User' }}
            </template>
            <template #content>
              <form @submit.prevent="saveUser" class="space-y-4">
                <div>
                  <label for="username" class="block text-sm font-medium mb-2">Username</label>
                  <InputText
                    id="username"
                    v-model="model.username"
                    class="w-full"
                    placeholder="Enter username"
                  />
                </div>
                
                <div>
                  <label for="email" class="block text-sm font-medium mb-2">Email</label>
                  <Textarea
                    id="email"
                    v-model="model.email"
                    class="w-full"
                    :rows="3"
                    placeholder="Enter email"
                  />
                </div>
                
                <div>
                  <Button 
                    type="submit" 
                    label="Save User" 
                    icon="pi pi-save"
                    class="w-full"
                  />
                </div>
              </form>
            </template>
          </Card>
          
          <div v-if="errors.length > 0" class="mt-4">
            <Message 
              v-for="error in errors" 
              :key="error" 
              severity="error" 
              :closable="false"
              class="mb-2"
            >
              {{ error }}
            </Message>
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
    for (const [field, message] of Object.entries(errorObj.response.data.errors)) {
      errors.value.push(`${field}: ${message}`)
    }
  } else if (errorObj?.message) {
    errors.value.push(errorObj.message)
  }
}
</script>

<style scoped>
.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 4rem 2rem;
  text-align: center;
  margin-bottom: 2rem;
}

.container {
  max-width: 1200px;
}

.grid {
  display: grid;
}

.grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr));
}

@media (min-width: 1024px) {
  .lg\:grid-cols-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
  
  .lg\:col-span-3 {
    grid-column: span 3 / span 3;
  }
  
  .lg\:col-span-1 {
    grid-column: span 1 / span 1;
  }
}

.gap-4 {
  gap: 1rem;
}

.space-y-4 > * + * {
  margin-top: 1rem;
}

.text-4xl {
  font-size: 2.25rem;
  line-height: 2.5rem;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.font-bold {
  font-weight: 700;
}

.font-medium {
  font-weight: 500;
}

.text-gray-600 {
  color: #6b7280;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.mt-4 {
  margin-top: 1rem;
}

.mb-4 {
  margin-bottom: 1rem;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.block {
  display: block;
}

.flex {
  display: flex;
}

.w-full {
  width: 100%;
}
</style>
