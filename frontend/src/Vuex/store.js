// src/Vuex/store.js
import { createStore } from "vuex";

export default createStore({
  state() {
    return {
      successAlerts: [],
      user: {
        token: null,
        roles: []
      },
      theatres: []
    };
  },

  mutations: {
    addSuccessAlert(state, message) {
      state.successAlerts.push(message);
    },
    removeSuccessAlert(state, index) {
      state.successAlerts.splice(index, 1);
    },
    setUser(state, userData) {
      localStorage.setItem("user", JSON.stringify(userData));
      state.user = userData;
    },
    setTheatres(state, value) {
      state.theatres = value;
    }
  },

  getters: {
    getSuccessAlert(state) {
      return state.successAlerts;
    },
    getRoles(state) {
      return state.user?.roles || [];
    },
    getToken(state) {
      return state.user?.token;
    },
    getTheatres(state) {
      return state.theatres;
    }
  },

  actions: {
    async getTheatres(context) {
      try {
        const response = await fetch(import.meta.env.VITE_BASEURL + "theatre", {
          headers: {
            "Authentication-Token": context.getters.getToken
          }
        });
        const data = await response.json();
        context.commit("setTheatres", data);
      } catch (error) {
        console.error("Error fetching theatres:", error);
      }
    }
  }
});

