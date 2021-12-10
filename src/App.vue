<template>
  <div id="app">
    <tr v-for="mod in mods" :key="mod.link">
        <td>
            <input type="checkbox" v-model="mod.enabled" @click="check(mod.id,mod.enabled)">
        </td>
        <td>
          <div class="frame">

            <img :src="mod.image" alt="">
          </div>
        </td>
        <td>
        <h2>
            <a :href="mod.link">{{mod.name}}</a>
        </h2>
            <p>
                {{mod.description}}
            </p>
        </td>
    </tr>  
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      mods: []
    }
  },
  methods:{
    check(id, enabled)
    {
      this.axios.post('http://localhost/minecraft/server/public/api/save.php',{id:id, enabled:!enabled}).then((response) => {
      })
    }
  },
  created(){
    this.axios.post('http://localhost/minecraft/server/public/api/get.php')
      .then(({data}) => {
        this.mods = data
      })
  }
}
</script>

<style> 

.frame {
    height: 25px;      /* Equals maximum image height */
    width: 160px;
    white-space: nowrap; /* This is required unless you put the helper span closely near the img */

    text-align: center;
    margin: 1em 0;
}

img {
    background: #3A6F9A;
    vertical-align: middle;
    max-height: 500px;
    max-width: 500px;
}
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    text-align: left;
    padding:10px;
    vertical-align:center;
}

tr:nth-child(even) {
    background-color: #ddd;
}


input[type=checkbox] {
    width: 25px;
    height: 25px;
    -moz-appearance: none;
    margin-left:50px;
}
</style>
