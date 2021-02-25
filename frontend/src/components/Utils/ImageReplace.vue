<template>
    <div class="image-replace">
        <div v-if="!src" :title="alt" :class="classes" class="image-replace__replace">
            {{ initials }}
        </div>
        <img
            v-else
            class="image-replace__img"
            :src="src"
            :alt="alt || name"
        />
    </div>
</template>

<script>
export default {
    name: 'ImageReplace', 
    props: {
        src: String,
        name: String,
        alt: String,
        variant: String
    },
    computed: {
        classes() {
            const base = 'image-replace__replace--'
            let classes = []
    
            if (this.variant) {
                let variants = this.variant.split(' ')
                classes = classes.concat(variants.map(variant => base + variant))
            }

            return classes
        },
        initials() {
            if (!this.name) {
                return
            }

            const words = this.name.replace(/^\s+|\s+$/g, '').split(' ')
            let initials = ''
            
            const firstLetter = words[0][0]
            if (firstLetter) {
                initials = firstLetter
            }

            if (words.length > 1) {
                const firstLetterOfLastWord = words[words.length - 1][0]
                initials += firstLetterOfLastWord
            }
            else {
                const secondLetter = words[0][1]
                if (secondLetter) {
                    initials += secondLetter
                }
            }
            return initials.toUpperCase()
        }
    }
}
</script>

<style lang="scss" scoped>
    .image-replace {
        position: relative;

        &,
        &__img,
        &__replace {
            width: 100%;
            height: 100%;
        }

        &__img {
            object-fit: cover;
        }

        &__replace {
            color: white;
            background-color: $color-green;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Work Sans', sans-serif;
            font-size: 30px;

            &--white {
                color: $color-green;
                background-color: white;
            }

            &--small {
                font-size: 20px;
            }

            &--rounded {
                border-radius: 50%;
            }
        }
    }
</style>