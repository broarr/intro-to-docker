import { default as baseTheme } from '@mdx-deck/themes';

const { colors } = baseTheme;

export default {
    ...baseTheme,
    colors: {
        ...colors,
        code: colors.text,
    },
};
