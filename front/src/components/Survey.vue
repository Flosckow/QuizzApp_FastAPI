<template>
    <div class="left-ads-display col-lg-9">
      <h1>List Survey</h1>
        <div class="row">
          <div v-for="survey in listSurvey" :key="survey.id" class="col-md-4 product-men">
            <div class="product-shoe-info editContent text-center mt-lg-4">
              <div class="item-info-product">
                <h4 class="">
                  <a href="#" @click="goTo(survey.id)" class="editContent">{{ survey.title}}</a>
                </h4>
              </div>
            </div>
          </div>
        </div>
    </div>
</template>


<script>
export default {
  name: 'Survey',
    data() {
      return {
        listSurvey: [],
      }
    },
    methods: {
      async loadListSurvey() {
      this.listSurvey = await fetch(`http://127.0.0.1:8000/survey/all?skip=0&limit=100`
        ).then(response => response.json()
        ).then(response => {
          return response
        })
      },
      goTo(id) {
        this.$router.push({ name: 'SurveySingle', params: {id: id} })
      },
    },
    created() {
      this.loadListSurvey(this.page)
    },
}
</script>


<style scoped>
  .editContent {
    padding-left: 3rem;
    padding-right: 3rem;
  }
</style>