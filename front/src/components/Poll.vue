<template>
    <div class="left-ads-display col-lg-9">
      <h1>List Poll</h1>
      <div class="row">
        <div v-for="poll in listPoll" :key="poll.id" class="col-md-4 product-men">
          <div class="product-shoe-info editContent text-center mt-lg-4">
            <div class="item-info-product">
              <h4 class="">
                <a href="#" @click="goTo(poll.id)" class="editContent">{{poll.title}}</a>
              </h4>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>


<script>
export default {
  name: 'Poll',
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
      goTo(id) {
        this.$router.push({ name: 'One_poll_action', params: {id: id} })
      },
    },
    created() {
      this.loadListPoll(this.page)
    },
}
</script>


<style scoped>
  .editContent {
    padding-left: 3rem;
    padding-right: 3rem;
  }
</style>