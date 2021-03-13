<template>
  <div class="sideFrom">
    <h1>Hello {name}</h1>
    <div class="viewAll">
      <p>Список всех голосований которые вы создали {allPost}</p>
      <div v-for="poll in listPoll" :key="poll.id" class="col-md-4 product-men">
        <h4 class="">
          <a href="#" @click="goTo(poll.id)" class="editContent">{{poll.title}}</a>
        </h4>
      </div>
      <div class="actions">
        <button @click="goCreatePoll" class="button">CreatePoll</button>
        <button @click="goCreateSurvey" class="button">CreateSurvey</button>
      </div>



</template>


<script>
export default {
  name: 'PersonalOffice',
    data() {
      return {
        listPoll: [],
      }
    },
    methods: {
      async loadListPoll() {
        this.listPoll = await fetch(`http://127.0.0.1:8000/poll/all?skip=0&limit=100`
        ).then(response => response.json()
        ).then(response => {
          return response
        })
      },
      goCreatePoll () {
          this.$router.push({ name: 'CreatePoll' })
      },
      goCreateSurvey () {
          this.$router.push({ name: 'CreateSurvey' })
      }
    },
    created() {
      this.loadListPoll(this.page)
    },
}

<style>

</style>