import axios from 'axios'

let $axios = axios.create({
  // TODO: for some reasone devServer.proxy setting
  // in the vue.config.js doesn't work
  // https://cli.vuejs.org/config/#devserver
  // So temporary, we set the full URL here
  // baseURL: 'http://localhost:5000/api/',
  baseURL: 'http://localhost:5000/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' },
})

// Request Interceptor
$axios.interceptors.request.use(function(config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(
  function(response) {
    return response
  },
  function(error) {
    // Handle Error
    return Promise.reject(error)
  },
)

export interface User {
  id: String
  username: String
  email: String
}

export let backend = {
  getUsers() {
    return $axios.get(`users/`).then((response) => response.data)
  },

  getUser(id) {
    return $axios.get(`user/${id}`).then((response) => response.data)
  },

  createUser(data) {
    let user = {
      username: data.username,
      email: data.email,
    }
    return $axios.post(`users/`, user).then((response) => response.data)
  },

  updateUser(id, data) {
    let user = {
      username: data.username,
      email: data.email,
    }
    return $axios.post(`users/${id}`, user).then((response) => response.data)
  },

  deleteUser(id) {
    return $axios.delete(`users/${id}`).then((response) => response.data)
  },
}
