<template>
    <form v-on:submit.prevent="submitPoll" method="POST" class="mt-5" >
        <h3>Попробуйте создать свой опрос</h3>
        <label for="fname">Введите название вопроса:</label>
        <br><input type="text" id="title" name="title" ><br>
        <label for="fname">Введите название описание:</label>
        <br><input type="text" id="description" name="description" ><br>
        <label for="fname">Введите id survey:</label>
        <br><input type="text" id="survey_id" name="survey_id" ><br>
        <br><input type="submit" value="Отправить"><br>
    </form>
</template>

<script>
export default {
  name: 'CreatePoll',
    data() {
      return {
        title: '',
        description: '',
        survey_id: 0
      }
    },
    methods: {
      submitPoll() {
        const formData = { 'title': this.title,
                           'description': this.description,
                           'survey_id': this.survey_id
                         }
        fetch('http://127.0.0.1:8000/poll/',
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