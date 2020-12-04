<template>
  <div class="custom">
    <div class="btn-group">
        <button @click="goPoll" class="button">Poll</button>
        <button @click="goSurvey" class="button">Survey</button>
        <button @click="goCreatePoll" class="button">CreatePoll</button>
        <button @click="goCreateSurvey" class="button">CreateSurvey</button>
        <button @click="goCreateUser" class="button">Create User</button>
        <button @click="goLoginUser" class="button">Login User</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  methods: {
    goPoll () {
      this.$router.push({ name: 'Poll' })
    },
    goSurvey () {
      this.$router.push({ name: 'Survey' })
    },
    goCreatePoll () {
      this.$router.push({ name: 'CreatePoll' })
    },
    goCreateSurvey () {
      this.$router.push({ name: 'CreateSurvey' })
    },
    goCreateUser () {
      this.$router.push({ name: 'Registration' })
    },
    goLoginUser () {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.btn-group .button {
  background-color: #4CAF50; /* Green */
  border: 1px solid green;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  float: left;
}

.btn-group .button:not(:last-child) {
  border-right: none; /* Prevent double borders */
}

.btn-group .button:hover {
  background-color: #3e8e41;
}
</style>