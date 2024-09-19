<script lang="ts">
    import { slide } from 'svelte/transition';

    export let visible: boolean;
</script>

{#if visible}
<div transition:slide={{delay: 100, duration: 600}} class=" overflow-hidden pl-4">
    <slot></slot>
</div>
{/if}