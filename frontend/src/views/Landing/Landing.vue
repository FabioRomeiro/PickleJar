<template>
  <div class="landing">
    <div class="landing__wrapper">
      <div class="landing__logo">
        <Logo variant="big" />      
      </div>
      <div class="landing__box">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from '@/components/Logo/Logo.vue';

export default {
	name: 'Landing',
	components: { Logo }
};
</script>

<style lang="scss" scoped>
.landing {
	width: 100%;
	height: 100vh;
	background-color: $color-green;
	display: flex;
  flex-direction: column;
	align-items: center;

	&__box {
    width: 100%;
		max-width: 600px;
		background-color: white;
		padding: spacing(3);
		border-radius: 3px;
	}

  &__logo {
    margin-bottom: spacing(4);
  }

  &__wrapper {
    margin-top: 10vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-sizing: border-box;
    width: 80%;
  }
}
</style>