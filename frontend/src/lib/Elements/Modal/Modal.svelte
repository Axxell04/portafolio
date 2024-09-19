<script lang="ts">
    import { slide } from "svelte/transition";
    import { modalVisible, imgModal } from "../../../stores/store";

    const close = () => {
        modalVisible.set(false);
    }
</script>

{#if $modalVisible}
<button transition:slide={{delay: 200, duration: 500, axis: "x"}} on:click={close} class=" fixed backdrop-blur-md : bg-neutral-900/70  w-dvw h-dvh flex  place-content-center place-items-center hover:cursor-default p-4">
    {#if $imgModal}
        <div class="max-h-dvh p-4 flex">
            <img src={$imgModal} alt="" class=" max-h-full object-contain rounded">
        </div>
    {/if}
</button>
{/if}