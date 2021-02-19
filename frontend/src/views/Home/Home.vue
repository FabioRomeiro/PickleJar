<template>
	<div class="home">
		<Toolbar />
		<div class="home__wrapper">
			<router-view/>
		</div>
	</div>
</template>

<script>
import Toolbar from '@/components/Toolbar/Toolbar.vue'

export default {
	name: "Home",
	components: {
		Toolbar
	}
};
</script>

<style lang="scss" scoped>
	.home {
		&__wrapper {
			max-width: 1080px;
			width: 90%;
			margin: 0 auto;
			margin-top: spacing(5);
		}
	}
</style>