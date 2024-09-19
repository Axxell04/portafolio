<script lang="ts">
  import { Icon } from "svelte-icons-pack";
  import Technology from "../Technology.svelte";
  import { modeEditor, dataToUpdate, imagesToUpload, URLServer, imagesToDelete } from "../../../stores/store";

  import ImgProject from "../ImgProject.svelte";
  import { isContentProjectInterface, type ContentProjectInterface } from "../Interfaces/ContentFileInterface";
  import { FiExternalLink } from "svelte-icons-pack/fi";
  import { BsGithub } from "svelte-icons-pack/bs";
  
  export let nameFile: string;
  export let content: ContentProjectInterface;
  imagesToUpload.set(null)
  imagesToDelete.set([])

  function updateDataFile (e: Event, section: string) {
    if (e.target != null && "value" in e.target && typeof e.target.value === "string") {
      let value:string = e.target.value;
      dataToUpdate.update(data => {
        if (isContentProjectInterface(data?.content)) {
          if (section === "name") {
            data.content.name = value;
          } else if (section === "description") {
            data.content.description = value;
          } else if (section === "technologys") {
            let technologys = value.split(",")
            technologys = technologys.map((tech) => tech.trim())
            technologys = technologys.filter((tech) => tech)
            data.content.technologys = technologys
          } else if (section === "url") {
            data.content.url = value;
          } else if (section === "github") {
            data.content.github = value;
          }
        }

        return data;
      })
    }
  }

  function addImages (e: Event) {
    const target = e.target as HTMLInputElement
    if (target && target.files instanceof FileList) {
      imagesToUpload.set(target.files)
    }
  }
</script>
  
<div class="flex flex-1 flex-col gap-3 text-lg text-zinc-400">
  <div>
    <h2 class="font-bold">Nombre del proyecto</h2>
    {#if $modeEditor === "read"}
    <p>{content.name}</p>
    {:else if $modeEditor === "edit"}
    <input on:input={e => updateDataFile(e, "name")} class=" bg-zinc-800 w-full outline-none" type="text" value={content.name}>
    {/if}
  </div>
  
  <div>
    <h2 class="font-bold">Descripción del proyecto</h2>
    {#if $modeEditor === "read"}
    <p>{content.description}</p>
    {:else if $modeEditor === "edit"}
    <textarea on:input={e => updateDataFile(e, "description")} class="bg-zinc-800 w-full outline-none" id="">{content.description}</textarea>
    {/if}
  </div>
  
  <div>
    <h2 class="font-bold">Tecnologías utilizadas</h2>
    {#if $modeEditor === "read"}
      <div class="flex flex-row gap-4 py-3 flex-wrap">
      {#if "technologys" in content}
        {#each content.technologys as technology}
          <Technology name={technology} />
        {/each}
      {/if}
      </div>
    {:else if $modeEditor === "edit"}  
    <input class="outline-none bg-zinc-800 w-full" type="text" value={"technologys" in content ? [...content.technologys] : ""} on:input={e => updateDataFile(e, "technologys")}>
    {/if}
  </div>
  <div>
    {#if $modeEditor === "read" && content.url}
    <a href={content.url} target="_blank" class="flex flex-row gap-2 bg-neutral-400 justify-center text-zinc-900 p-2 rounded align-middle hover:bg-neutral-300">
      <Icon src={FiExternalLink} size={22}/>
      <span class="font-semibold">Acceder al proyecto</span>
    </a>
    {:else if $modeEditor === "edit"}
    <div class="flex flex-col gap-1 p-1">
      <label class="font-bold" for="url_project">URL </label>
      <input class="bg-zinc-800 hover:outline-none" type="text" name="url_project" on:input={e=>updateDataFile(e, "url")} value={content.url ? content.url : ""}>
    </div>
    {/if}
  </div>
  <div>
    {#if $modeEditor === "read" && content.github}
    <a href={content.github} target="_blank" class="flex flex-row gap-2 bg-neutral-400 justify-center text-zinc-900 p-2 rounded align-middle hover:bg-neutral-300">
      <Icon src={BsGithub} size={22}/>
      <span class="font-semibold">Ver repositorio</span>
    </a>
    {:else if $modeEditor === "edit"}
    <div class="flex flex-col gap-1 p-1">
      <label class="font-bold" for="github_project">GitHub </label>
      <input class="bg-zinc-800 hover:outline-none" type="text" name="github_project" on:input={e=>updateDataFile(e, "github")} value={content.github ? content.github : ""}>
    </div>
    {/if}
  </div>
  <div class="flex flex-col gap-2">
    <h2 class="font-bold pb-1 border-b border-zinc-800">Capturas</h2>
    {#if $modeEditor === "edit"}
    <div class="flex flex-col gap-1 place-items-center">
      <label class="font-medium" for="new_img">Agregar imagenes</label>
      <input name="new_img" class="w-fit rounded p-1 hover:cursor-pointer bg-zinc-800 outline-none" type="file" multiple accept=".jpg,.png" on:input={e=>addImages(e)}>
    </div>
    {/if}
  </div>

  <div class="flex flex-row flex-wrap gap-4 place-content-center">
    {#if content.images}
      {#each content.images as image}
        <ImgProject src={`${$URLServer}/static/img/${nameFile}/${image}`} name={image}/>
      {/each}
    {/if}
  </div>
</div>