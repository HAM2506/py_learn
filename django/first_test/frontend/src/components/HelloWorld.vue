<template>
  <div class="hello">
    <p v-text="count"></p>
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      count: 0
    }
  },
  mounted() {
    this.$ajax.get('api/get_hello/').then((response) => {
      this.count = response.data.data.times;
    }).catch(function (error) {
      console.log(error);
    });


    $.ajax({
        url:'api/get_hello/',
        type:'get',
        dataType:'json',
        success: (data) => {
          this.count = data.data.times;
        }
    })
    
    var d = {
      text: 'hello, world!'
    }

    $.ajax({
        url:'api/get_helloCount/',
        type:'get',
        dataType:'json',
        data: d,
        success: (data) => {
          console.log(data)
        }
    })
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
