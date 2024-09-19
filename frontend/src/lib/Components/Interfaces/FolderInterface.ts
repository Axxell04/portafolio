import type { FileInterface } from "./FileInterface"
export interface FolderInterface {
    type: string
    id: string
    name: string
    files: FileInterface[]
}

export function isFolderInterface(obj: any): obj is FolderInterface {
    return (typeof obj === "object" && obj != null) &&
        (typeof obj.type === "string") &&
        (typeof obj.id === "string") &&
        (typeof obj.name === "string") &&
        (Array.isArray(obj.files))
}