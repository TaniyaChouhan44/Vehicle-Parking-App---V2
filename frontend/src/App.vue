<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useStore } from 'vuex'

// Use composition API properly
const store = useStore()

onMounted(() => {
  const user = localStorage.getItem("user")
  if (user) {
    store.commit("setUser", JSON.parse(user))
  }
})
</script>

<template>
  <div
    class="alert alert-success alert-dismissible fade show"
    role="alert"
    v-for="(alert, i) in store.getters.getSuccessAlert"
    :key="i"
  >
    {{ alert }}
    <button
      type="button"
      class="btn-close"
      @click="store.commit('removeSuccessAlert', i)"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>
  <RouterView />
</template>
