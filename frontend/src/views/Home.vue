<template>
  <div class="home">
    <b-row class="shadow-lg p-3 mb-5 rounded col-sm">
      <main-card title="Stock Data" custom ="card shadow col-lg-8"><stock-card custom="bg-primary"></stock-card></main-card>
      <main-card title="Twitter Data" custom ="card shadow col-lg-4"><twitter-card custom = "bg-secondary"></twitter-card></main-card>
      <main-card title="News Articles" custom ="card shadow col-lg-12"><news-card custom = "bg-warning"></news-card></main-card>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import MainCard from '@/components/MainCard.vue'
import StockCard from '@/components/StockCard.vue'
import TwitterCard from '@/components/TwitterCard.vue'
import NewsCard from '@/components/NewsCard.vue'
export default {
  name: 'Home',
  components: {
    'main-card': MainCard,
    'stock-card': StockCard,
    'twitter-card': TwitterCard,
    'news-card': NewsCard
  },
}
</script>
