<template>
	<div class="toolbar">
        <Logo class="toolbar__logo" />

		<CredentialSearch class="toolbar__search" />
	</div>
</template>

<script>
import Logo from '@/components/Logo/Logo.vue';
import CredentialSearch from '@/components/Toolbar/CredentialSearch.vue';

export default {
	name: 'Toolbar',
	components: {
		Logo,
		CredentialSearch
    }
}
</script>

<style scoped lang="scss">
.toolbar {
	display: flex;
	justify-content: space-between;
	align-items: center;
	width: calc(100% - #{spacing(3)} * 2);
	height: 70px;
	padding: 0 spacing(3);
	background-color: $color-green;
	color: white;

	&__search {
		flex-grow: 1;
		max-width: 600px;
		margin: 0 spacing(3);
	}
}
</style>
