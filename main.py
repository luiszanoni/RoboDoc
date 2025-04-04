import automation.desktop_automation as desktop
import automation.file_handler as file
import automation.ocr_processor as ocr
import automation.web_scraper as scraper

print("#################################")
print("      BEM VINDO AO AUTOBOT       ")
print("#################################")

def menu():
    print("\nFUNCOES")
    print("1 - DESKTOP AUTOMATION ")
    print("2 - MANIPULADOR DE ARQUIVO ")
    print("3 - OCR PROCESSOR ")
    print("4 - WEB SCRAPER ")
    print("5 - SAIR")

menu()

while True:
    escolha = input("Escolha a funcao desejada: ")
    try:
        escolha = int(escolha)
    except ValueError:
        print("Opção inválida! Digite um número entre 1 e 5.")
        continue
    if escolha == 1:

        print("\nIniciando Desktop Automation...\n")
        automacao = desktop.DesktopAutomation()
        automacao.automatizacaopaint()
        menu()

    elif escolha == 2:

        auto = file.FileHandler()

        print("\nFUNCOES DO FILE HANDLER\n")
        print("1 - Verificar se arquivo tem registros duplicados ")
        print("2 - Identificar os registros duplicados ")
        print("3 - Excluir os registros duplicados ")
        print("4 - Transformar arquivo json -> xlsx (excel) ")
        print("5 - Transformar arquivo json -> csv")
        print("6 - Transformar arquivo json -> xml")
        escolhaFile = input("Escolha a funcao do FileHandler desejada: ")
        try:
            escolhaFile = int(escolhaFile)
        except ValueError:
            print("Opção inválida! Digite um número entre 1 e 5.")
            continue
        if escolhaFile == 1:
            auto.verificaDuplicados()
        elif escolhaFile == 2:
            auto.indentificaDuplicados()
        elif escolhaFile == 3:
            auto.excluiDuplicados()
        elif escolhaFile == 4:
            auto.converteParaXlsx()
        elif escolhaFile == 5:
            auto.converteParaCsv()
        elif escolhaFile == 6:
            auto.converteParaXml()
        menu()

    elif escolha == 3:

        ocr.transcreverCurriculo()
        menu()

    elif escolha == 4:

        scraper.procuraPreco()
        menu()

    elif escolha == 5:

        print("Saindo do programa . . . ")
        break

    else:
        print("Opção inválida! Digite um número entre 1 e 5.")