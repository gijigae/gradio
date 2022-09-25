import gradio as gr


def greet(name):
    return "Hello " + name + "!!"


demo = gr.Interface(
    fn=greet, inputs=gr.component("textarea"), outputs=gr.component("textarea")
)


if __name__ == "__main__":
    demo.launch()
