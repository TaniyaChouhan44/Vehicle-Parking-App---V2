<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark px-4">
    <router-link to="/user/home" class="navbar-brand">ParkingApp</router-link>

    <div class="collapse navbar-collapse justify-content-end">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link to="/user/lots" class="nav-link">Parking Lots</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/user/reservations" class="nav-link">My Reservations</router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click="logout" style="cursor:pointer">Logout</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function logout() {
  localStorage.clear()
  router.push('/login')
}
</script>
