<template>
    <form v-on:submit.prevent="submitSurvey" method="POST" class="mt-5" >
        <h3>Попробуйте создать свое голосование</h3>
        <label for="fname">Введите название вопроса:</label>
        <br><input type="text" id="title" name="title" ><br>
        <label for="fname">Введите описание:</label>
        <br><input type="text" id="description" name="description" ><br>
        <br><input type="submit" value="Отправить"><br>
    </form>
</template>

<script>
export default {
  name: 'CreateSurvey',
    data() {
      return {
        title: '',
        description: ''
      }
    },
    methods: {
      submitSurvey() {
        const formData = { 'title': this.title,
                           'description': this.description
                         }
        fetch('http://127.0.0.1:8000/survey/',
          {method: "POST",
          body: JSON.stringify(formData),
          headers: {     'Access-Control-Allow-Origin': true,   },}
        ).then( (resp) => {
          console.log('SUCCESS!!')
          console.log(resp)
        }).catch( (e) => {
          console.log('FAILURE!!')
          console.log(e)
        })
      }
    }
  }
</script>