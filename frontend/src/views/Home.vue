<template>
  <div class="container">
    <b-row class="p-3 ">
      <main-card title="Stock Graph" custom ="card shadow col-lg-7 col-md-5 col-sm-12 col-xs-12 p-1 m-2" >
        <stock-card custom=""></stock-card>
      </main-card>
      <main-card title="Toggle" custom ="card shadow col-lg-4 col-md-5 col-sm-12 col-xs-12  p-1 m-2">
        <b-row>
        <toggle-card custom = "bg-warning rounded mb-2 container shadow col-lg- 12 col-md-6" ticker = "AMD" ></toggle-card>
        <toggle-card custom = "bg-success rounded mb-2 container shadow col-lg- 12 col-md-6" ticker = "AAPL"></toggle-card>
      </b-row>
      <b-row>
        <toggle-card custom = "bg-danger rounded mb-2 container shadow col-lg- 12 col-md-6" ticker = "SPLK"></toggle-card>
        <toggle-card custom = "bg-info rounded  container shadow col-lg- 12 col-md-6" ticker = "TSLA"></toggle-card>
      </b-row>
      </main-card>
    </b-row>
    <b-row class="p-3 ">
      <main-card title="Twitter Card" custom ="card shadow col-lg-6 col-md-6 col-sm-12 col-xs-12 p-1 "><twitter-card></twitter-card></main-card>
      <main-card title="Sentiment Card" custom ="card shadow col-lg-6  col-md-6 col-sm-12 col-xs-12 p-1"><sentiment-card custom = "bg-secondary" ></sentiment-card></main-card>

    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import MainCard from '@/components/MainCard.vue'
import StockCard from '@/components/StockCard.vue'
import TwitterCard from '@/components/TwitterCard.vue'
import ToggleCard from '@/components/ToggleCard.vue'
import SentimentCard from '@/components/SentimentCard.vue'

export default {
  name: 'Home',
  components: {
    'main-card': MainCard,
    'stock-card': StockCard,
    'twitter-card': TwitterCard,
    'toggle-card': ToggleCard,
    'sentiment-card': SentimentCard
  },
  data(){

    return {

    }
  }
}
</script>
