<template>
    <div class="security-status-badge" :class="classes">
        {{ status }}
    </div>
</template>

<script>
export default {
    name: 'SecurityStatusBadge',
    props: {
        size: {
            type: String,
            validator: (size) => ['small', 'big'].includes(size.toLowerCase()),
            default: 'small'
        }
    },
    computed: {
        classes() {
            return ['security-status-badge--' + this.status, 'security-status-badge--' + this.size]
        },
        status() {
            return 'safe'
        }
    }
}
</script>

<style lang="scss" scoped>
    .security-status-badge {
        display: inline-flex;
        border-radius: 4px;
        padding: 4px spacing(1);
        text-transform: capitalize;
        font-weight: $font-weight-regular;
        color: white;

        &--small {
            font-size: 12px;
        }

        &--big {
            font-size: 24px;
        }

        &--safe {
            background-color: $color-blue;
        }
    }
</style>