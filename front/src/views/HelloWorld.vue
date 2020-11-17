<template>
  <div class="custom">
    <a href="#" class="editContent">Welcome to Test</a>
    <ul>
      <li><button @click="goPoll" class="login">Poll</button></li>
      <li><button @click="goSurvey" class="login">Survey</button></li>
      <li><button @click="goCreatePoll" class="login">CreatePoll</button></li>
      <li><button @click="goCreateSurvey" class="login">CreateSurvey</button></li>
    </ul>
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
      this.$router.push({ name: 'CreateSurvey'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
