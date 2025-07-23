import axios from 'axios'

const $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' },
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(
  function (response) {
    return response
  },
  function (error) {
    // Handle Error
    return Promise.reject(error)
  },
)

export interface User {
  id: string
  username: string
  email: string
}

export interface UserCreateData {
  username: string
  email: string
}

export interface ApiResponse<T> {
  data: T
}

export const backend = {
  getUsers(): Promise<ApiResponse<User[]>> {
    return $axios.get('users/').then((response) => response.data)
  },

  getUser(id: string): Promise<ApiResponse<User>> {
    return $axios.get(`users/${id}`).then((response) => response.data)
  },

  createUser(data: UserCreateData): Promise<ApiResponse<User>> {
    const user = {
      username: data.username,
      email: data.email,
    }
    return $axios.post('users/', user).then((response) => response.data)
  },

  updateUser(id: string, data: UserCreateData): Promise<ApiResponse<User>> {
    const user = {
      username: data.username,
      email: data.email,
    }
    return $axios.post(`users/${id}`, user).then((response) => response.data)
  },

  deleteUser(id: string): Promise<ApiResponse<User>> {
    return $axios.delete(`users/${id}`).then((response) => response.data)
  },
}
