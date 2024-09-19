import {isContentBlankInterface, isContentProjectInterface, type ContentBlankInterface, type ContentProjectInterface} from './ContentFileInterface'
export interface FileInterface {
    type: string
    id: string
    id_folder: string | null
    template: string
    name: string
    content: ContentBlankInterface | ContentProjectInterface
}

export function isFileInterface(obj: any): obj is FileInterface {
    return (typeof obj === "object" && obj != null) &&
        (typeof obj.type === "string") &&
        (typeof obj.id === "string") &&
        (typeof obj.id_folder === "string" || obj.id_folder === null) &&
        (typeof obj.template === "string") &&
        (typeof obj.name === "string") &&
        (isContentBlankInterface(obj.content) || isContentProjectInterface(obj.content))
}