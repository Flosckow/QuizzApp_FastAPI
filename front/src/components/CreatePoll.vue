<template>
    <form v-on:submit.prevent="submitPoll" method="POST" class="mt-5" >
        <h3>Попробуйте создать свой опрос</h3>
        <label for="fname">Введите название вопроса:</label>
        <br><input type="text" id="title" name="title" v-model="title"><br>
        <label for="fname">Введите название описание:</label>
        <br><input type="text" id="description" name="description" v-model="description"><br>
        <label for="fname">Введите id survey:</label>
        <br><input type="text" id="survey_id" name="survey_id" v-model="survey_id"><br>
        <label for="fname">Введите вопросы:</label>
        <br><input type="text" id="q" name="q" v-model="questions.q"><br>
        <label for="fname">Количество баллов за вопрос:</label>
        <br><input type="text" id="max_points" name="max_points" v-model="questions.max_points"><br>
        <label for="fname">Введите ответы:</label>
        <br><input type="text" id="text" name="text" v-model="questions.answers.text"><br>
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
        survey_id: '',
        questions: {
            q: '',
            max_points: '',
            visible: 'true',
            answers: [
                {
                    text: 'ересь'
                }
            ],
        },
      }
    },
    methods: {
      submitPoll() {
        const formData = {
            "title": this.title,
            "description": this.description,
            "survey_id": this.survey_id,
            "questions": [this.questions],
        }
        fetch('http://127.0.0.1:8000/poll/',
          {method: "POST",
          body: JSON.stringify(formData),
          }
        ).then( (resp) => {
          console.log('SUCCESS!!')
          console.log(formData)
          console.log(resp)
        }).catch( (e) => {
          console.log('FAILURE!!')
          console.log(e)
        })
      }
    }
  }
</script>