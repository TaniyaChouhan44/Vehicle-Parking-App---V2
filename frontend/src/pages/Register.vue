<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { ref } from 'vue'
import { useStore } from 'vuex'

const router = useRouter()
const store = useStore()

const form = ref({
  username: '',
  fname: '',
  lname: '',
  email: '',
  password: ''
})

const error = ref({
  username: '',
  fname: '',
  lname: '',
  email: '',
  password: ''
})

function clearErrors() {
  error.value = {
    username: '',
    fname: '',
    lname: '',
    email: '',
    password: ''
  }
}

function validate() {
  clearErrors()
  let isValid = true

  if (!form.value.fname.trim()) {
    error.value.fname = 'First name is required.'
    isValid = false
  }

  if (!form.value.lname.trim()) {
    error.value.lname = 'Last name is required.'
    isValid = false
  }

  if (form.value.password.length < 2) {
    error.value.password = 'Minimum password length is 2 characters.'
    isValid = false
  }

  return isValid
}

async function signup() {
  if (!validate()) return

  try {
    const res = await fetch(import.meta.env.VITE_BASEURL + 'auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form.value)
    })

    const data = await res.json()

    if (res.ok) {
      store.commit('addSuccessAlert', 'User registered successfully.')
      router.push('/login')
    } else {
      if (data.msg?.includes('exists')) {
        error.value.email = data.msg
        error.value.username = data.msg
      }
    }
  } catch (err) {
    console.error('Registration error:', err)
    error.value.email = 'Server error. Try again later.'
  }
}
</script>


<template>
  <h1 class="text-center mb-4">Sign up</h1>
  <form @submit.prevent="signup" class="w-100" style="max-width: 500px; margin: auto;">
    <div class="mb-3 row align-items-center">
      <label for="username" class="col-sm-4 col-form-label">Username:</label>
      <div class="col-sm-8">
        <input type="text" class="form-control" id="username" v-model="form.username" required />
        <div class="invalid-feedback" v-show="error.username">{{ error.username }}</div>
      </div>
    </div>

    <div class="mb-3 row align-items-center">
      <label for="fname" class="col-sm-4 col-form-label">First Name:</label>
      <div class="col-sm-8">
        <input type="text" class="form-control" id="fname" v-model="form.fname" required />
        <div class="invalid-feedback" v-show="error.fname">{{ error.fname }}</div>
      </div>
    </div>

    <div class="mb-3 row align-items-center">
      <label for="lname" class="col-sm-4 col-form-label">Last Name:</label>
      <div class="col-sm-8">
        <input type="text" class="form-control" id="lname" v-model="form.lname" required />
        <div class="invalid-feedback" v-show="error.lname">{{ error.lname }}</div>
      </div>
    </div>

    <div class="mb-3 row align-items-center">
      <label for="email" class="col-sm-4 col-form-label">Email:</label>
      <div class="col-sm-8">
        <input type="email" class="form-control" id="email" v-model="form.email" required />
        <div class="invalid-feedback" v-show="error.email">{{ error.email }}</div>
      </div>
    </div>

    <div class="mb-3 row align-items-center">
      <label for="password" class="col-sm-4 col-form-label">Password:</label>
      <div class="col-sm-8">
        <input type="password" class="form-control" id="password" v-model="form.password" required />
        <div class="invalid-feedback" v-show="error.password">{{ error.password }}</div>
      </div>
    </div>

    <div class="text-center">
      <input type="submit" class="btn btn-primary" value="Register" />
    </div>

    <div class="text-center mt-3">
      <router-link :to="{ name: 'login' }" class="text-decoration-none text-primary">
        Already have an account? Login
      </router-link>
    </div>
  </form>
</template>


<style scoped>
.invalid-feedback {
  display: block !important;
}
</style>
