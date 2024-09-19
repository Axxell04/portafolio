<script lang="ts">
    import { Icon } from "svelte-icons-pack";
    import { modalVisible, imgModal, modeEditor, imagesToDelete } from "../../stores/store";
    import { VscChromeClose, VscTrash } from "svelte-icons-pack/vsc";
    export let src: string;
    export let name: string;

    const openImg = () => {
        imgModal.set(src);
        modalVisible.set(true);
    }

    function deleteImg () {
        imagesToDelete.set([...$imagesToDelete, name])
    }

    $: isDeleting = $imagesToDelete.includes(name)

    function cancelDelete () {
        imagesToDelete.set($imagesToDelete.filter((img) => img != name))
    }

</script>

<div class="relative rounded flex items-center justify-center">
    <button on:click={openImg}>
        <img class="rounded max-h-96 max-w-full object-contain" src={src} alt="">
    </button>
    {#if $modeEditor === "edit"}
    <div class=" bg-slate-500">
        <button class=" flex place-items-center absolute bottom-0 right-0 rounded-tl bg-zinc-900 text-red-500 hover:text-red-600" on:click={isDeleting ? cancelDelete : deleteImg}>
            <Icon src={isDeleting ? VscChromeClose : VscTrash} size={35}/>
        </button>
    </div>
    {/if}
</div>