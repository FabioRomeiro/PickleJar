<template>
    <svg class="logo-draw" :class="`logo-draw--${size}`" width="31" height="44" viewBox="0 0 31 44" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect y="5" width="31" height="39" rx="6" fill="white"/>
        <rect y="5" width="31" height="39" rx="6" fill="white"/>
        <rect y="5" width="31" height="39" rx="6" fill="white"/>
        <rect y="5" width="31" height="39" rx="6" fill="white"/>
        <rect y="5" width="31" height="39" rx="6" fill="white"/>
        <rect y="5" width="31" height="39" rx="6" fill="white"/>
        <rect y="5" width="31" height="39" rx="6" fill="white"/>
        <rect y="5" width="31" height="39" rx="6" fill="white"/>
        <rect y="5" width="31" height="39" rx="6" fill="white"/>
        <rect x="2" y="23.9435" width="6" height="18" rx="3" transform="rotate(-29.3788 2 23.9435)" fill="#3FEC7A"/>
        <rect x="23.5574" y="18.5889" width="6" height="18" rx="3" transform="rotate(23.4559 23.5574 18.5889)" fill="#3FEC7A"/>
        <path d="M20.8154 12.8482C22.1205 11.8275 24.0059 12.058 25.0267 13.3631C26.0474 14.6682 25.8169 16.5536 24.5118 17.5744L15.0595 24.9672C13.7544 25.9879 11.869 25.7574 10.8482 24.4523C9.82748 23.1472 10.058 21.2618 11.3631 20.241L20.8154 12.8482Z" fill="#3FEC7A"/>
        <rect x="2" width="27" height="6" rx="2" fill="white"/>
        <rect x="2" width="27" height="6" rx="2" fill="white"/>
        <rect x="2" width="27" height="6" rx="2" fill="white"/>
        <rect x="2" width="27" height="6" rx="2" fill="white"/>
        <rect x="2" width="27" height="6" rx="2" fill="white"/>
        <rect x="2" width="27" height="6" rx="2" fill="white"/>
        <rect x="2" width="27" height="6" rx="2" fill="white"/>
        <rect x="2" width="27" height="6" rx="2" fill="white"/>
        <rect x="2" width="27" height="6" rx="2" fill="white"/>
    </svg>
</template>

<script>
export default {
    name: 'LogoSvg',
    props: {
        size: String
    }
}
</script>

<style lang="scss" scoped>
    .logo-draw {
        &--big {
            width: 60px;
            height: 70px;
        }
    }
</style>