<template>
  <div id="app">
    <h1>Every Dream</h1>
    <router-view />
    <Browse></Browse>
    <Slideimg></Slideimg>
    <Slide2></Slide2>
    <h1>Your Dream</h1>
    <main>それはあなたのもう一つの物語です。</main>
    <About></About>
    <Home></Home>
  </div>
</template>

<script>
import About from './components/AboutView.vue'
import Home from './components/HomeView.vue'
import Browse from './components/Browser.vue'
import Slideimg from './components/SlideShow.vue'
import Slide2 from './components/SlideShow2.vue'

export default {
  name: 'app',
  components:{
    About,
    Home,
    Browse,
    Slideimg,
    Slide2
  }
}
</script>

<style>
#app {
  text-align: center;
  color: rgb(255, 255, 255);
  background-color: black;
}
</style>