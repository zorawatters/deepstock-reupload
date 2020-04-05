<template>
  <div class="home">
    <b-row class="shadow-lg p-3 mb-5 rounded col-sm">
      <main-card title="Stock" custom ="card shadow col-lg-8"><stock-card custom="bg-primary"></stock-card></main-card>
      <main-card title="Toggle" custom ="card shadow col-lg-4"><toggle-card custom = "bg-warning"></toggle-card></main-card>
      <main-card title="Twitter Card" custom ="card shadow col-lg-12"><twitter-card custom = "bg-secondary"></twitter-card></main-card>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import MainCard from '@/components/MainCard.vue'
import StockCard from '@/components/StockCard.vue'
import TwitterCard from '@/components/TwitterCard.vue'
import ToggleCard from '@/components/ToggleCard.vue'
export default {
  name: 'Home',
  components: {
    'main-card': MainCard,
    'stock-card': StockCard,
    'twitter-card': TwitterCard,
    'toggle-card': ToggleCard
  },
}
</script>
