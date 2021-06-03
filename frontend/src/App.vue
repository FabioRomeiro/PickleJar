<template>
	<div id="app">
		<Alert />
		<router-view />
	</div>
</template>

<script>
import Alert from '@/components/Global/Alert'

export default {
	components: {
		Alert
	}
}
</script>

<style lang="scss">
	body { }
</style>
