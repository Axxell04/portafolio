<script lang="ts">
  import { Icon, type IconType } from "svelte-icons-pack";
  
  export let name: string;
  export let icon: IconType;
  export let url: string;

</script>
<a href={url} target="_blank" class="flex flex-row gap-1 bg-neutral-400 rounded-full py-1 px-2 hover:bg-neutral-300">
    <Icon src={icon} size={25}/>
    <span class="font-semibold">{name}</span>
  </a>