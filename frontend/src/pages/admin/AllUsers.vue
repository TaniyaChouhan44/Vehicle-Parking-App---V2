<template>
  <div class="container mt-5">
    <h2 class="text-center mb-4">All Registered Users</h2>
    <table class="table table-bordered table-striped">
      <thead class="table-dark">
        <tr>
          <th>ID</th>
          <th>Username</th>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Email</th>
          <th>Role</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.fname }}</td>
          <td>{{ user.lname }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.role }}</td>
        </tr>
      </tbody>
    </table>

    <div v-if="error" class="alert alert-danger mt-3 text-center">
      {{ error }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const users = ref([])
const error = ref('')

onMounted(async () => {
  try {
    const token = localStorage.getItem('token')
    const res = await fetch(import.meta.env.VITE_BASEURL + 'admin/users', {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
      }
    })

    const data = await res.json()

    if (!res.ok) {
      error.value = data.msg || 'Failed to load users'
      return
    }

    users.value = data
  } catch (err) {
    console.error(err)
    error.value = 'Server error. Please try again later.'
  }
})
</script>

<style scoped>
.table th, .table td {
  vertical-align: middle;
  text-align: center;
}
</style>
