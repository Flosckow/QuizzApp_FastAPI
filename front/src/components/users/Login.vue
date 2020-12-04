<template>
  <form class="custom-style" method="POST" @submit.prevent="enterUser">
    <div class="container">
      <div class="row justify-content-center mb-5 mt-5">
        <div class="col-md-3 col-md-offset-3 text-center">
          <div class="align-self-center">
            <label for="text">Вход</label>
          </div>
          <div class="form group">
            <label for="username">Ваш email:</label>
            <input type ="username" class="form-control" id="username" placeholder="Введите email:" required v-model="user.username">
          </div>
          <div class="form group">
            <label for="password">Ваш password:</label>
            <input type ="password" class="form-control" id="password" placeholder="Введите password:" required v-model="user.password">
          </div>
          <button type="submit" class="btn btn-primary">Войти</button>
        </div>
      </div>
    </div>
  </form>
</template>


<script>
export default {
  name: 'Login',
    data(){
      return {
        user: {
          username: '',
          password: ''
        }
      }
    },
	methods: {
      enterUser() {
        fetch('http://127.0.0.1:8000/auth/jwt/login',
          {method: "POST",
          body: new URLSearchParams({
            'username': this.user.username,
            'password': this.user.password,
          }),
          headers: {     'Access-Control-Allow-Origin': true,   },}
        ).then( (resp) => {
          console.log('SUCCESS!!')
          console.log(resp)
        }).catch( (e) => {
          console.log('FAILURE!!')
          console.log(e)
        })
      },
	}
 }
</script>

<style>
  .form-group {
    position: absolute
  }
  .btn btn-primary {
    margin-left: 5px
  }
  .custom-style {
    padding:10px;
    border-radius:10px;
  }
</style>