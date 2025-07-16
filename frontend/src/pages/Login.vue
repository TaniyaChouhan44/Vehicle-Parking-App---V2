<template>
  <div class="container mt-5">
    <h2 class="text-center mb-4">Login</h2>
    <form @submit.prevent="login" class="w-100" style="max-width: 500px; margin: auto;">

      <div class="mb-3 row align-items-center">
        <label for="email" class="col-sm-4 col-form-label">Email:</label>
        <div class="col-sm-8">
          <input
            type="email"
            class="form-control"
            id="email"
            v-model="email"
            required
            placeholder="abcd@example.com"
          />
          <div class="text-danger mt-1" v-if="error">{{ error }}</div>
        </div>
      </div>

      <div class="mb-3 row align-items-center">
        <label for="password" class="col-sm-4 col-form-label">Password:</label>
        <div class="col-sm-8">
          <input
            type="password"
            class="form-control"
            id="password"
            v-model="password"
            required
            placeholder="password"
          />
        </div>
      </div>

      <div class="text-center">
        <button type="submit" class="btn btn-primary w-50">Login</button>
      </div>

      <div class="text-center mt-3">
        <router-link :to="{ name: 'signup' }" class="text-decoration-none text-primary">
          Don't have an account?
        </router-link>
      </div>
    </form>
  </div>
</template>

<script>
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { ref } from 'vue'

export default {
  setup() {
    const email = ref('')
    const password = ref('')
    const error = ref('')
    const router = useRouter()
    const store = useStore()

    const login = async () => {
      error.value = ''

      try {
        const res = await fetch(import.meta.env.VITE_BASEURL + 'auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: email.value, password: password.value })
        })

        const data = await res.json()

        if (!res.ok) {
          error.value = data.msg || 'Invalid credentials'
          return
        }

        // Store token and user info
        localStorage.setItem('token', data.access_token)
        localStorage.setItem('role_id', data.role_id)

        store.commit('setUser', {
          token: data.access_token,
          username: data.username,
          email: data.email,
          role_id: data.role_id
        })

        // Redirect based on role_id
        if (data.role_id === 1) {
          router.push('/admin/home')
        } else if (data.role_id === 2) {
          router.push('/user/home')
        } else {
          error.value = 'Unknown role'
        }

      } catch (err) {
        console.error(err)
        error.value = 'Server error. Please try again later.'
      }
    }

    return {
      email,
      password,
      error,
      login
    }
  }
}
</script>

<style scoped>
.text-danger {
  font-size: 0.9rem;
}
</style>
