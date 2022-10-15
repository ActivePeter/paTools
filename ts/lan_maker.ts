export namespace lan{
    function split_str(str:string){
        if(str.indexOf("_")!=-1){
            return str.split("_")
        }
        return [str]
    }
    export function to_UpperCamelCase(str:string){
        return split_str(str)
            //使用trim摆脱任何多余的空间
            .map(a => a.trim())
            //将每个单词的第一个字符转换为大写
            .map(a => a[0].toUpperCase() + a.substring(1))
            //将所有字符串重新连接在一起
            .join("")
    }
    export enum BasicValueType{
        String,
        Int,
        Float,
        Array,
        Obj,
    }
    export class ValueType{
        constructor(public basic:BasicValueType) {
        }
    }
    export function ValueTypeTsName(t:ValueType){
        switch (t.basic){
            case lan.BasicValueType.Float:
                return "number"
            case lan.BasicValueType.Int:
                return "number"
            case lan.BasicValueType.String:
                return "string"
            case lan.BasicValueType.Obj:
                return "any"
            case lan.BasicValueType.Array:
                return "any[]"
        }
        return ""
    }
    export function ValueTypeRsName(t:ValueType){
        switch (t.basic){
            case lan.BasicValueType.Float:
                return "f32"
            case lan.BasicValueType.Int:
                return "i32"
            case lan.BasicValueType.String:
                return "String"
            case lan.BasicValueType.Obj:
                return "serde_json::Map<String,serde_json::Value>"
            case lan.BasicValueType.Array:
                return "Vec<serde_json::Value>"
        }
        return ""
    }
    interface ICodeNode{
        to_ts_string():string
        to_rs_string():string
    }
    export class Node_Arg implements ICodeNode{
        constructor(
            private argname:string,
            private typename:string) {
        }

        to_ts_string(): string {
            return this.argname+":"+this.typename;
        }

        to_rs_string(): string {
            return this.argname+":"+this.typename;
        }
    }
    export class Node_Class implements ICodeNode{
        values:{
            name:string,
            type:ValueType
        }[]=[]

        constructor(private name:string) {
        }
        to_ts_string(): string {
            return "export class "+this.name+"{\n"
                +"constructor("
                +this.values.map((v,i)=>{
                    return (i==0?"":"\n")+"public "+v.name+":"+ValueTypeTsName(v.type)
                })
                +"){}\n}\n"
                ;
        }
        add_value(name:string,type:ValueType){
            this.values.push({
                name,type
            })
        }

        to_rs_string(): string {
            return "pub struct "+this.name+"{"
                +this.values.map((v,i)=>{
                    return (i==0?"":"\n")+"pub "+v.name+":"+ValueTypeRsName(v.type)
                })
                +"}"
                ;
        }
    }
    export class Node_Func implements ICodeNode{
        args:Node_Arg[]=[]
        add_arg(arg:Node_Arg){
            this.args.push(arg)
            return this
        }
        constructor(private fname:string) {
        }
        body:undefined|string
        set_body(body:undefined|string){
            this.body=body

            return this
        }
        to_ts_string(): string {
            return this.fname+"("+
                this.args.map((arg,i)=>{
                    return (i==0?"":"")+arg.to_ts_string()
                })
                +"):void"+(this.body?this.body:"");
        }
        to_rs_string(): string {
            return ""
                ;
        }
    }
    export class Node_Interface implements ICodeNode{
        funcs:Node_Func[]=[]
        export=false
        set_export(){
            this.export=true
        }
        add_func(f:Node_Func){
            this.funcs.push(f)
            return this
        }
        constructor(private name:string) {
        }

        to_ts_string(): string {
            let make=this.export?"export ":""+"interface "+this.name+"{\n"
            this.funcs.forEach((f)=>{
                make+=f.to_ts_string()+";\n"
            })
            make+="}"
            return make;
        }
        to_rs_string(): string {
            return ""
                ;
        }
    }
    export class Node_Text implements ICodeNode{
        to_ts_string(): string {
            return this.txt;
        }
        to_rs_string(): string {
            return this.to_ts_string()
                ;
        }
        constructor(private txt:string) {
        }
    }
    export class Node_Some implements ICodeNode{
        lines:ICodeNode[]=[]
        // classes:Node_Class[]=[]
        add_func(f:Node_Func){
            this.lines.push(f)
            return this
        }
        add_class(c:Node_Class){
            this.lines.push(c)
            return this
        }
        add_node(c:ICodeNode){
            this.lines.push(c)
            return this
        }
        to_ts_string(): string {
            let make=""
            this.lines.forEach((f)=>{
                make+=f.to_ts_string()+"\n"
            })
            // this.classes.forEach((c)=>{
            //     make+=c.to_ts_string()+"\n"
            // })
            return make;
        }
        to_rs_string(): string {
            let make=""
            this.lines.forEach((f)=>{
                make+=f.to_rs_string()+"\n"
            })
            // this.classes.forEach((c)=>{
            //     make+=c.to_ts_string()+"\n"
            // })
            return make;
        }
    }
}
