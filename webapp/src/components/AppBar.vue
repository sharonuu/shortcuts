<template>
  <div class="app-bar">
    <span class="app-bar_l" @click="$emit('left')">
      <i :class="['fas', `fa-${left}`]"></i>
    </span>
    <h1>{{ title }}</h1>
    <span class="app-bar_r" @click="$emit('right')">
      <i :class="['fas', `fa-${right}`]"></i>
    </span>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: ''
    },
    left: {
      type: String,
      default: 'chevron-left'
    },
    right: {
      type: String,
      default: 'ellipsis-v'
    }
  }
}
</script>

<style lang="scss">
.app-bar {
  display: flex;
  align-items: center;
  height: 50px;
  font-size: 20px;
  z-index: 1;

  h1 {
    display: flex;
    justify-content: center;
    flex: 1;
  }
  span {
    padding: 0 20px;
  }
}
</style>
