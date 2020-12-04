<template>
  <form v-on:submit.prevent="registerUser" method="POST" class="mt-5" >
    <div class="container">
      <div class="row justify-content-center mb-5 mt-5">
        <div class="col-md-3 col-md-offset-3 text-center">
          <div class="align-self-center">
            <label for="text">Регистарция</label>
          </div>
          <div class="form group">
            <label for="name">Ваш name:</label>
            <input type ="text" class="form-control" id="name" placeholder="Введите name:" v-model="user.name">
          </div>
          <div class="form group">
            <label for="email">Ваш email:</label>
            <input type ="email" class="form-control" id="email" placeholder="Введите email:"  v-model="user.email">
          </div>
          <div class="form group">
            <label for="password">Ваш password:</label>
            <input type ="password" class="form-control"
                id="password" placeholder="Введите password:"
                v-model="user.password">
          </div>
          <div class="form group">
            <label for="password2">Подтвердите password:</label>
            <input type ="password" @blur="$v.user.confirmPassword.$touch()" :class="{'is-invalid': $v.user.confirmPassword.$error}" class="form-control" id="confirmPassword"
            placeholder="Введите password:"  v-model="user.confirmPassword">
          </div>
          <div :class="{'is-invalid': $v.user.confirmPassword.$error}">
            <small>Пароли должны совпадать</small>
          </div>
          <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
        </div>
      </div>
    </div>
  </form>
</template>


<script>
import { required , sameAs, minLength} from 'vuelidate/lib/validators';
export default {
  name: 'Registration',
    data() {
      return {
        user: {
          email: '',
          password: '',
          name: '',
          confirmPassword: ''
        }
      }
    },
    validations: {
      user: {
		password: {
          required,
          minLength: minLength(6)
        },
          confirmPassword: { required, sameAsPassword: sameAs('password') }
      }
   },
    methods: {
      registerUser () {
        const formData = {'password': this.user.password,
                          'email': this.user.email,
                          'name': this.user.name}
        fetch('http://127.0.0.1:8000/auth/register',
          {method: "POST",
          body: JSON.stringify(formData),
          headers: {     'Access-Control-Allow-Origin': true,   },}
        ).then( (resp) => {
          console.log('SUCCESS!!')
          console.log(resp)
          console.log(formData)
        }).catch( (e) => {
          console.log('FAILURE!!')
          console.log(e)
        })
      }
    }
  }
</script>


<style scoped>
    .error {
        color: red;
    }
</style>