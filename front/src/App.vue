<template>
  <div id="app">
    <HelloWorld/>
    <router-view/>
  </div>
</template>

<script>
import HelloWorld from './views/HelloWorld.vue'

export default {
  name: 'app',
  components: {
    HelloWorld
  }
}
</script>

<style>
</style>
