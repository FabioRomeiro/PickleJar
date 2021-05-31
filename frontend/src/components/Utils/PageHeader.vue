<template>
	<div class="page-header">
		<h3 class="page-header__title">
			<i class="material-icons icon">{{ icon }}</i>
			<span>{{ title }}</span>
		</h3>
		<div class="page-header__actions">
			<slot></slot>
		</div>
	</div>
</template>

<script>
export default {
	props: {
		icon: String,
		title: String
	}
}
</script>

<style lang="scss">
    .page-header {
        .header-button {
            margin-right: spacing(2);

            &:last-child {
                margin-right: 0;
            }
        }
    }
</style>

<style lang="scss" scoped>
	.page-header {
		width: 100%;
		display: flex;
        align-items: center;
        justify-content: space-between;

		&__title {
			font-size: 24px;
			font-weight: $font-weight-medium;
			display: inline-flex;
			align-items: center;
			position: relative;
			margin-bottom: spacing(3);

			&::after {
				content: '';
				position: absolute;
				width: 100%;
				height: 2px;
				border-radius: 3px;
				background-color: rgba($color-green-dark, 1);
				box-shadow: 0 0 3px $color-green, 0 0 2px inset $color-green;
				left: 0;
				bottom: -#{spacing(1)};
			}

			.icon {
				margin-right: spacing(1);
				color: $color-green-dark;
				filter: drop-shadow(0 0 2px rgba($color-green, .5));
			}
		}

		&__actions {
			
			.action-button {
				margin-right: spacing(2);

				&:last-child {
					margin-right: 0;
				}
			}
		}
	}
</style>