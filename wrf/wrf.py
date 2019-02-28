#!/usr/bin/env python
# -*- coding: utf8 -*-


"""Windows Registry Fixer

This is a module composed by functions that
are used to create a file with entries to
Windows' Regedit.
After the file's creation, the user is able
to import-it in Regedit.

"""


__author__ = "José Lopes de Oliveira Júnior <jlojunior (at) gmail.com>"
__license__ = "GPLv3"


#    Windows Registry Fixer
#    Copyright (C) 2009  José Lopes de Oliveira Júnior
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys


# SECTION NETWORK
# SUB-SECTION CLIENTS

def autorun(on=0):
    
    """Controle da Funcao de Auto-Execucao do CD-ROM
    
    DESCRIPTION
        Normalmente quando voce insere um disco no drive de CD-ROM, o conteudo 
    e executado automaticamente. Esta funcao lhe permite desabilitar este
    comportamento.
    
    COMPATIBILITY
        Windows NT/2000/XP
    
    MODIFIED VALUES
        Autorun : dword : 00000000 = Desabilita a Auto-Execucao;
    00000001 = Habilita a Auto-Execucao.
    
    """
    
    if on: 
        return '''[HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\\
CDRom]
"Autorun"=dword:00000001'''
    
    else: 
        return '''[HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\\
CDRom]
"Autorun"=dword:00000000'''

# SECTION NETWORK
# SUB-SECTION CLIENTS

def cached_logons_count(numb=0):
    
    """Contador de Logons em Cache
    
    DESCRIPTION
        Determina quantas contas de usuários o Windows armazenara no cache de
    logon do computador local. O Windows armazena estes dados para serem usados
    em caso do PDC estar fora do ar.
        Se este valor for igual a 0, o Windows não salvara qualquer dado da
    conta em no computador local. Neste caso, se o PDC estiver fora do ar e
    algum usuario tentar se logar no domino, a seguinte mensagem sera exibida:
        "O sistema nao pode loga-lo porque o domínio <Nome-Dominio> nao esta
    disponivel."
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        CachedLogonsCount : string = Determina o numero de logons que serao
    armazenados em cache, variando de 0 a 50.
    
    OBSERVATION
        O computador deve ser reiniciado para que a alteração tenha efeito.
        
    """
    
    return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\Current\
Version\\Winlogon]
"CachedLogonsCount"="%d"''' % numb

def delete_roaming_cache(on=0):
    
    """Deletar Copias em Cache de Perfis Remotos
    
    DESCRIPTION
        Esta configuracao permite que o Windows delete o cache do perfil de
    quaisquer usuarios remotos quando eles executarem log off do sistema. Isto
    ajudara a manter a integridade do perfil de usuario e a economizar espaco 
    em disco onde ha varios usuarios moveis.
    
    COMPATIBILITY
        Windows NT/2000/XP
    
    MODIFIED VALUES
        DeleteRoamingCache : dword : 00000000 = Desabilita a exclusao do cache;
    00000001 = Habilita a exclusao do cache.
    
    """
    
    if on: 
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\\
CurrentVersion\\Winlogon]
"DeleteRoamingCache"=dword:00000001'''
    
    else: 
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\\
CurrentVersion\\Winlogon]
"DeleteRoamingCache"=dword:00000000'''

# SECTION NETWORK
# SUB-SECTION SERVERS

def srv_comment(com=''):
    
    """Mostrar Descricao do Computador na Rede Local
    
    DESCRIPTION
        Esta entrada lhe permite adicionar uma descricao do computador para ser
    mostrado na sua rede local.
    
    COMPATIBILITY
        Windows 2000
    
    MODIFIED VALUES
        srvcomment : string : Adicionar a descricao do computador.
        
    """
    
    return '''[HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\\
lanmanserver\\parameters]
"srvcomment"="%s"''' % com

# SECTION SECURITY
# SUB-SECTION CONTROL PANEL

def show_admin_tools(on=0):
    
    """Mostrar Ferramentas Administrativas no Painel de Controle
    
    DESCRIPTION
        Esta entrada lhe permite definir se o applet "Ferramentas
    Administrativas" e mostrado no Painel de Controle.
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED KEYS
        {D20EA4E1-3957-11d2-A40B-0C5020524153} : Deve ser deletado/criado para
    esconder/mostrar as Ferramentas administrativas.
    
    """
    
    if on: 
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\Explorer\\ControlPanel\\NameSpace\\{D20EA4E1-3957-11d2-A40B-\
0C5020524153}]'''
    
    else: 
        return '''[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\Explorer\\ControlPanel\\NameSpace\\{D20EA4E1-3957-11d2-A40B-\
0C5020524153}]'''

# SECTION SECURITY
# SUB-SECTION LOGIN AND AUTHENTICATION

def dont_disp_last_username(on=0):
    
    """Inibir a Exibicao do Nome do Ultimo Usuario Logado
    
    DESCRIPTION
        Esta restricao remove a habilidade de visualizar qual foi o ultimo
    usuario logado no sistema, limpando o seu nome na tela de login.
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        DontDisplayLastUserName : dword : 00000000 = Padrao;
    00000001 = Remove o nome do usuario.
    
    """
    
    if on: 
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"DontDisplayLastUserName"=dword:00000001'''
    
    else: 
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"DontDisplayLastUserName"=dword:00000000'''

def welcome_text(title="WRF"):
    
    """Customizar a Janela de Logon e o Titulo do Dialogo de Seguranca
    
    DESCRIPTION
        Este ajuste permite adicionar textos no titulo da janela de logon 
    padrao e na caixa de dialogo de seguranca do Windows.
    
    COMPATIBILITY
        Windows NT/2000/XP
    
    MODIFIED VALUES
        Welcome : string : Texto a ser adicionado.
        
    """
    
    return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\\
CurrentVersion\\Winlogon]
"Welcome"="%s"''' % title

def logon_prompt(msg="Modified with Windows Registry Fixer"): 
    
    """Alterar a Mensagem Mostrada na Tela de Logon
    
    DESCRIPTION
        Voce pode personalizar (ou legalizar) a mensagem mostrada na caixa de
    logon acima do nome de usuario e senha.
    
    COMPATIBILITY
        Windows NT/2000/XP
    
    MODIFIED VALUES
        LogonPrompt : string : Texto a ser adicionado.
        
    """
    return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\\
CurrentVersion\\Winlogon]
"LogonPrompt"="%s"''' % msg

def shutdown_without_logon(on=0):
    
    """Habilitar Desligamento a Partir da Caixa de Dialogo de Logon
    
    DESCRIPTION
        Quando este ajuste esta habilitado, o botao de desligamento e mostrado
    na caixa de dialogo de autenticacao quando o sistema inicia. Isto permite
    que o sistema seja desligado sem que algum usuario se autentique nele. Esta
    opcao e ativada por padrao em estacoes de trabalho e desativada em
    servidores.
    
    COMPATIBILITY
        Windows NT/2000/XP
    
    MODIFIED VALUES
        ShutdownWithoutLogon : dword : 00000000 = Desabilita o desligamento;
    00000001 = Habilita o desligamento no logon.
    
    """
    
    if on :
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\policies\\system]
"ShutdownWithoutLogon"=dword:00000001'''
    
    else :
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\policies\\system]
"ShutdownWithoutLogon"=dword:00000000'''

def legal_notice(caption="WRF", text="Modified with Windows Registry Fixer"):
    
    """Nota Legal Antes do Logon
    
    DESCRIPTION
        Use estes campos para criar uma caixa de dialogo que sera mostrada para
    todos os usuarios antes de se logarem no sistema. Isto e util quando voce
    quer avisar ao usuario que e ilegal tentar se logar sem permissao.
    
    COMPATIBILITY
        Windows NT/2000/XP
    
    MODIFIED VALUES
        LegalNoticeCaption : string : Titulo da caixa de dialogo.
        LegalNoticeText : string : Conteudo da caixa de dialogo (a mensagem).
    """
    
    return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\\
CurrentVersion\\Winlogon]
"LegalNoticeCaption"="%s"
"LegalNoticeText"="%s"''' % (caption, text)

# SECTION WINDOWS
# SUB-SECTION TROUBLESHOOTING

def disable_system_recovery_tools(on=0):
    
    """Desabilita as Ferramentas de Restauracao do Sistema e Configuracoes
    
    DESCRIPTION
        A restauracao do sistema permite aos usuarios reverter configuracoes do
    Windows para um ponto anterior (chamados "Pontos de Restauracao"). Esta
    entrada pode ser usado para restringir o acesso dos usuarios a essas
    ferramentas e configuracoes.
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED VALUES
        DisableConfig : dword : 00000000 = Desabilitado;
    00000001 = Remove opcoes do menu iniciar.
        DisableSR : dword : 00000000 = Desabilitado;
    00000001 = Desabilita as restauracoes do sistema.
    
    """
    
    if on: 
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows \
NT\\SystemRestore]
"DisableConfig"=dword:00000001
"DisableSR"=dword:00000001'''
    
    else: 
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows \
NT\\SystemRestore]
"DisableConfig"=dword:00000000
"DisableSR"=dword:00000000'''

# SECTION SOFTWARE
# SUB-SECTION INTERNET EXPLORER

def remove_windows_messenger_from_ie(on=0): 
    
    """Remover o Windows Messenger do Internet Explorer
    
    DESCRIPTION
        Esta entrada pode ser usado para remover a integracao do Windows
    Messenger com o Internet Explorer. Isto removera o icone da barra de
    ferramentas e o item do menu Ferramentas.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED KEYS
        {FB5F1910-F110-11d2-BB9E-00C04F795683} : Deve ser removida para
    finalizar a integracao entre os softwares.
    
    """
    
    if on :
        return '''[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet \
Explorer\\Extensions\\{FB5F1910-F110-11d2-BB9E-00C04F795683}]'''
    
    else :
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet \
Explorer\\Extensions\\{FB5F1910-F110-11d2-BB9E-00C04F795683}]'''

# SECTION WINDOWS
# SUB-SECTION DESKTOP

def icons_visibility(on=0): 
    
    """Alterar a Visibilidade de Icones do Desktop
    
    DESCRIPTION
        Esta entrada lhe permite controlar quais icones sao visiveis no seu
    Desktop. Modificando o espaco de nome do Desktop voce pode adicionar ou
    remover icones especiais.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED KEYS
        {D20EA4E1-3957-11d2-A40B-0C5020524153} : Ferramentas Administrativas
        {85BBD92O-42A0-1O69-A2E4-08002B30309D} : Pasta
        {21EC2O2O-3AEA-1O69-A2DD-08002b30309d} : Painel de Controle
        {D20EA4E1-3957-11d2-A40B-0C5020524152} : Fontes
        {FF393560-C2A7-11CF-BFF4-444553540000} : Historico
        {00020D75-0000-0000-C000-000000000046} : Caixa de Entrada
        {00028B00-0000-0000-C000-000000000046} : Rede Microsoft
        {20D04FE0-3AEA-1069-A2D8-08002B30309D} : Meu Computador
        {450D8FBA-AD25-11D0-98A8-0800361B1103} : Meus Documentos
        {1f4de370-d627-11d1-ba4f-00a0c91eedba} : Computadores da Rede
        {7007ACC7-3202-11D1-AAD2-00805FC1270E} : Conexoes de Rede
        {2227A280-3AEA-1069-A2DE-08002B30309D} : Impressoras e Aparelhos de Fax
        {7be9d83c-a729-4d97-b5a7-1b7313c39e0a} : Diretorio de Programas
        {645FF040-5081-101B-9F08-00AA002F954E} : Lixeira
        {E211B736-43FD-11D1-9EFB-0000F8757FCD} : Scanners e Cameras
        {D6277990-4C6A-11CF-8D87-00AA0060F5BF} : Tarefas Agendadas
        {48e7caab-b918-4e58-a94d-505519c795dc} : Diretorio do Menu Iniciar
        {7BD29E00-76C1-11CF-9DD0-00A0C9034933} : Arquivos Temporarios de
    Internet
        {BDEADF00-C265-11d0-BCED-00A0C90AB50F} : Diretorios da Web
    
    OBSERVATION
        Cada sub-chave e um Identificador Unico Global (Globally Unique
    IDentifier - GUID) que representa um icone e o valor padrao e, usualmente,
    um nome legivel a humanos.
        Para deletar um icone do seu Desktop, basta remover a sua respectiva
    entrada no registro. Da mesma forma, para adicionar um icone, basta
    adicionar sua respectiva entrada no registro.
    
    """
    
    if on :
        return '''[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\Explorer\\Desktop\\NameSpace\\{D20EA4E1-3957-11d2-A40B-\
0C5020524153}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{85BBD92O-42A0-1O69-A2E4-08002B30309D}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{21EC2O2O-3AEA-1O69-A2DD-08002b30309d}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{D20EA4E1-3957-11d2-A40B-0C5020524152}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{FF393560-C2A7-11CF-BFF4-444553540000}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{00020D75-0000-0000-C000-000000000046}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{00028B00-0000-0000-C000-000000000046}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{20D04FE0-3AEA-1069-A2D8-08002B30309D}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{450D8FBA-AD25-11D0-98A8-0800361B1103}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{1f4de370-d627-11d1-ba4f-00a0c91eedba}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{7007ACC7-3202-11D1-AAD2-00805FC1270E}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{2227A280-3AEA-1069-A2DE-08002B30309D}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{7be9d83c-a729-4d97-b5a7-1b7313c39e0a}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{645FF040-5081-101B-9F08-00AA002F954E}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{E211B736-43FD-11D1-9EFB-0000F8757FCD}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{D6277990-4C6A-11CF-8D87-00AA0060F5BF}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{48e7caab-b918-4e58-a94d-505519c795dc}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{7BD29E00-76C1-11CF-9DD0-00A0C9034933}]
[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{BDEADF00-C265-11d0-BCED-00A0C90AB50F}]'''
    
    else :
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\Explorer\\Desktop\\NameSpace\\{D20EA4E1-3957-11d2-A40B-0C5020524153}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{85BBD92O-42A0-1O69-A2E4-08002B30309D}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{21EC2O2O-3AEA-1O69-A2DD-08002b30309d}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{D20EA4E1-3957-11d2-A40B-0C5020524152}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{FF393560-C2A7-11CF-BFF4-444553540000}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{00020D75-0000-0000-C000-000000000046}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{00028B00-0000-0000-C000-000000000046}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{20D04FE0-3AEA-1069-A2D8-08002B30309D}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{450D8FBA-AD25-11D0-98A8-0800361B1103}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{1f4de370-d627-11d1-ba4f-00a0c91eedba}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{7007ACC7-3202-11D1-AAD2-00805FC1270E}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{2227A280-3AEA-1069-A2DE-08002B30309D}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{7be9d83c-a729-4d97-b5a7-1b7313c39e0a}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{645FF040-5081-101B-9F08-00AA002F954E}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{E211B736-43FD-11D1-9EFB-0000F8757FCD}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{D6277990-4C6A-11CF-8D87-00AA0060F5BF}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{48e7caab-b918-4e58-a94d-505519c795dc}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{7BD29E00-76C1-11CF-9DD0-00A0C9034933}]
[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\\
Desktop\\NameSpace\\{BDEADF00-C265-11d0-BCED-00A0C90AB50F}]'''

# SECTION WINDOWS
# SUB-SECTION ACCESSORIES
# SUB-SECTION REGISTRY EDITOR

def show_admin_account(on=0): 
    
    """Exibir a Conta "Administrador" na Tela de Logon
    
    DESCRIPTION
        Ao se logar no Windows, a conta "Administrador" nao esta disponivel por
    padrao. Esta entrada permite adiciona-la na lista de contas.
    
    COMPATIBILITY
        Windows XP Professional
    
    MODIFIED VALUES
        Administrator : dword : 00000000 = Nao mostra a conta;
    00000001 = Mostra a conta.
    
    """
    
    if on :
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\\
CurrentVersion\\Winlogon\\SpecialAccounts\\UserList]
"Administrator"=dword:00000001'''
    
    else :
        return '''[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\\
CurrentVersion\\Winlogon\\SpecialAccounts\\UserList]
"Administrator"=dword:00000000'''

# SECTION WINDOWS
# SUB-SECTION SYSTEM

def no_auto_update(on=0): 
    
    """Gerenciar Atualizacoes Automaticas do Windows
    
    DESCRIPTION
        Esta configuracao lhe permite desabilitar as atualizacoes automaticas 
    do Windows.
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        NoAutoUpdate : dword : 00000000 = Atualizacoes habilitadas;
    00000001 = Desabilita atualizacoes.
    
    """
    
    if on :
        return '''[HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\\
Windows\\WindowsUpdate\\AU]
"NoAutoUpdate"=dword:00000001'''
    
    else :
        return '''[HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\\
Windows\\WindowsUpdate\\AU]
"NoAutoUpdate"=dword:00000000'''

# SECTION WINDOWS
# SUB-SECTION STARTUP AND SHUTDOWN

def clear_page_file_at_shutdown(on=0): 
    
    """Limpar Arquivo de Paginacao no Desligamento do Sistema
    
    DESCRIPTION
        O Windows normalmente nao limpa ou recria o arquivo de paginacao. Num
    sistema muito usado, isto pode acarretar na perda de seguranca e 
    desempenho. Habilitando esta configuracao, fara com que o Windows limpe o 
    arquivo de paginacao sempre antes de ser desligado.
    
    COMPATIBILITY
        Windows NT/2000/XP
    
    MODIFIED VALUES
        ClearPageFileAtShutdown : dword : 00000000 = Desabilitado;
    00000001 = Opcao habilitada.
    
    OBSERVATION
        A ativacao desta opcao aumenta o tempo de desligamento do micro em
    alguns segundos.
    
    """
    
    if on :
        return '''[HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\\
Session Manager\\Memory Management]
"ClearPageFileAtShutdown"=dword:00000001'''
    
    else :
        return '''[HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\\
Session Manager\\Memory Management]
"ClearPageFileAtShutdown"=dword:00000000'''

###
# LOCAL USER SETTINGS
###

# SECTION NETWORK
# SUB-SECTION CLIENTS

def exclude_profile_dirs(dirs=''): 
    
    """Prevenir o Upload de Diretorios Especificos para o Servidor de Perfis de
    Usuarios
    
    DESCRIPTION
        Quando perfis sao usados e o usuario executa log off de um dominio
    Windows, certos diretorios sao eviados para a central de perfis de usuarios
    no servidor. Esta configuracao lhe permite bloquear o envio de certos
    diretorios que possuem conteudos nao essenciais (e.g., Arquivos temporarios
    da Internet).
    
    COMPATIBILITY
        Windows NT/2000/XP
    
    MODIFIED VALUES
        ExcludeProfileDirs : string : Lista de diretorios a excluir separados
    por ponto e virgula (;).
    
    """
    
    return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows NT\\\
CurrentVersion\\Winlogon]
"ExcludeProfileDirs"="%s"''' % dirs

# SECTION SECURITY

def disable_current_user_run(on=0): 
    
    """Desabilitar Execucao de Comandos Especificados no Registro
    
    DESCRIPTION
        Esta restricao e usada para desabilitar a habilidade de executar
    programas de inicializacao especificados no registro quando o Windows e
    carregado.
    
    COMPATIBILITY
        Windows 98/Me/2000/XP
    
    MODIFIED VALUES
        DisableCurrentUserRun : dword : 00000000 = Habilita Execucao;
    00000001 = Desabilita Execucao.
        DisableCurrentUserRunOnce : dword : 00000000 = Habilita Execucao;
    00000001 = Desabilita Execucao.
    
    """
    
    if on :
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"DisableCurrentUserRun"=dword:00000001
"DisableCurrentUserRunOnce"=dword:00000001'''
    
    else :
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"DisableCurrentUserRun"=dword:00000000
"DisableCurrentUserRunOnce"=dword:00000000'''

def disallow_run(on=0, apps=[]): 
    
    """Retringir a Execucao de Aplicativos Especificos
    
    DESCRIPTION
        Este ajuste lhe permite especificar aplicacoes e nomes de arquivos que
    usuarios estao restringidos de executar.
    
    COMPATIBILITY
        Windows 2000/Me/XP
    
    MODIFIED VALUES
        DisallowRun : dword : 00000000 = Permite a execucao de todos
    aplicativos; 00000001 = Habilita restricao de aplicativos.
    
    """
    
    if on:
        ret = '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"DisallowRun"=dword:00000001
[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\\
Explorer\\DisallowRun]
'''
        
        n = 1
        for i in apps:
            ret += '"' + str(n) + '"="' + i + '"\n'
            n += 1
        
        return ret
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"DisallowRun"=dword:00000000
'''

def restrict_run(on=0, apps=[]): 
    
    """Restringir Aplicacoes que os Usuarios podem Executar
    
    DESCRIPTION
        O Windows lhe da a habilidade de restringir as aplicacoes que podem ser
    executadas pelos usuarios em uma estacao de trabalho.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        RestrictRun : dword : 00000000 = Permite a execucao de todos
    aplicativos; 00000001 = Habilita a restricao de execucao de aplicacoes.
    
    """
    
    if on:
        ret = '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"RestrictRun"=dword:00000001
[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\\
Explorer\\RestrictRun]
'''
        
        n = 1
        for i in apps:
            ret += '"' + str(n) + '"="' + i + '"\n'
            n += 1
        
        return ret
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"RestrictRun"=dword:00000000
'''

# SECTION SECURITY
# SUB-SECTION ACTIVE DESKTOP

def no_ad(on=0): 
    
    """Desabilitar Active Desktop
    
    DESCRIPTION
        Esta entrada incapacitara a utilizacao do Active Desktop.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoActiveDesktop : dword : 00000000 = Desabilita restricao;
    00000001 = Habilita restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoActiveDesktop"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoActiveDesktop"=dword:00000000'''

def no_set_ad(on=0): 
    
    """Remover Opcoes do Active Desktop do Menu Configuracoes
    
    DESCRIPTION
        Esta entrada removera as opcoes do Active Desktop das Configuracoes no
    Menu Iniciar.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoSetActiveDesktop : dword : 00000000 = Desabilita restricao;
    00000001 = Habilita restricao.
    
    """
    
    if on :
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSetActiveDesktop"=dword:00000001'''
    
    else :
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSetActiveDesktop"=dword:00000000'''

# SECTION SECURITY
# SUB-SECTION CONTROL PANEL

def no_control_panel(on=0): 
    
    """Desabilitar o Painel de Controle
    
    DESCRIPTION
        Esta configuracao lhe permite restringir o acesso dos usuarios as 
    opcoes do Painel de Controle.
    
    COMPATIBILITY
        Windows 2000/Me/XP
    
    MODIFIED VALUES
        NoControlPanel : dword : 00000000 = Desabilita restricao;
    00000001 = Habilita restricao.
    
    """
    
    if on :
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoControlPanel"=dword:00000001'''
    
    else :
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoControlPanel"=dword:00000000'''

def no_set_folders(on=0):
    
    """Esconder as Configuracoes Painel de Controle, Impressoras e Conexoes de
    Rede
    
    DESCRIPTION
        Esta restricao remove as configuracoes Painel de Controle, Impressoras 
    e Conexoes de Rede do menu Iniciar. Se as configuracoes da Barra de Tarefas
    tambem estiverem escondidas, acarretara na completa remocao das
    configuracoes.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoSetFolders : dword : 00000000 = Desabilita restricao;
    00000001 = Habilita restricao.
    
    OBSERVATION
        Esta restricao deve desabilitar tambem a hotkey do Windows Explorer
    (SUPER + E).
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSetFolders"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSetFolders"=dword:00000000'''

def no_choose_programs_page(on=0): 
    
    """Esconder "Definir Acesso e Padroes do Programa" em "Adicionar/Remover
    Programas"
    
    DESCRIPTION
        Esta restricao e usada para esconder a opcao "Definir Acesso e Padroes
    do Programa" na pagina "Adicionar/Remover Programas". Esta caracteristica
    foi introduzida com o Windows XP SP1 e o Windows 2000 SP3 para permitir aos
    usuarios configurar as aplicacoes padroes usadas no PC.
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        NoChooseProgramsPage : dword : 00000000 = Padrao;
    00000001 = Esconder opcao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Uninstall]
"NoChooseProgramsPage"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Uninstall]
"NoChooseProgramsPage"=dword:00000000'''

def no_disp_cpl(on=0): 
    
    """Negar Acesso as Configuracoes de Video
    
    DESCRIPTION
        Esta opcao desabilita o icone no do Painel de Controle de Configuracao
    de Video, negando aos usuarios acesso a quaisquer configuracoes de video.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoDispCPL : dword : 00000000 = Desabilitado; 00000001 = Habilitado.
        
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispCPL"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispCPL"=dword:00000000'''

# SECTION SECURITY
# SUB-SECTION CONTROL PANEL
# SUB-SECTION DISPLAY

def no_disp_bg_page(on=0):
    
    """Esconder a Pagina de Alteracao de Papel de Parede
    
    DESCRIPTION
        Esta opcao esconde a pagina de plano de fundo, evitando que os usuarios
    alterem o papel de parede por ali.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoDispBackgroundPage : dword : 00000000 = Padrao;
    00000001 = Habilita restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispBackgroundPage"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispBackgroundPage"=dword:00000000'''

def no_themes_tab(on=0): 
    
    """Esconder a Pagina de Ajuste de Temas
    
    DESCRIPTION
        Esta opcao esconde a tag Temas que previne que os usuarios selecionem 
    um tema alternativo. Temas normalmente incluem novos sons, icones, dentre
    outros elementos.
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED VALUES
        NoThemesTab : dword : 00000000 = Padrao; 00000001 = Habilita restricao.
        
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoThemesTab"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoThemesTab"=dword:00000000'''

def no_desktop_control_themes(on=0):
    
    """Restringir Controle dos Temas de Desktop
    
    DESCRIPTION
        Estas restricoes controlam o acesso aos ajustes de temas de Desktop,
    incluindo os estilos de janelas, botoes, esquemas e fontes.
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED VALUES
        NoColorChoice : dword : 00000000 = Desabilitado;
    00000001 = Desabilita o controle de "Esquemas de cores".
        NoSizeChoice : dword : 00000000 = Desabilitado;
    00000001 = Desabilita o controle de "Tamanho da fonte".
        NoVisualStyleChoice : dword : 00000000 = Desabilitado;
    00000001 = Desabilita o controle de "Janelas e botoes".
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoVisualStyleChoice"=dword:00000001
"NoColorChoice"=dword:00000001
"NoSizeChoice"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoVisualStyleChoice"=dword:00000000
"NoColorChoice"=dword:00000000
"NoSizeChoice"=dword:00000000'''

def no_change_animation(on=0):
    
    """Restringir Alteracoes nas Configuracoes de Animacao
    
    DESCRIPTION
        Esta restricao previne usuarios de selecionar a opcao de animar o
    movimentos de janelas e menus.
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        NoChangeAnimation : dword : 00000000 = Padrao;
    00000001 = Habilita restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoChangeAnimation"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoChangeAnimation"=dword:00000000'''

def no_disp_settings_page(on=0):
    
    """Esconder a Pagina Configuracoes de Video
    
    DESCRIPTION
        Esta opcao esconde a pagina "Configuracoes" do controle de propriedades
    de video.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoDispSettingsPage : dword : 00000000 = Desabilitado;
    00000001 = Habilitada restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispSettingsPage"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispSettingsPage"=dword:00000000'''

def no_disp_scr_sav_page(on=0):
    
    """Esconder a Pagina de Configuracoes de Protecao de Tela
    
    DESCRIPTION
        Esta opcao esconde a pagina "Protecao de Tela" do controle de
    configuracoes de video, o que inibe usuarios de alterarem as configuracoes
    de protecao de tela.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoDispScrSavPage : dword : 00000000 = Desabilitado;
    00000001 = Habilitada restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispScrSavPage"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispScrSavPage"=dword:00000000'''

def no_disp_appearance_page(on=0):
    
    """Esconder a Pagina Aparecia de Video
    
    DESCRIPTION
        Quando habilitado, este ajuste esconde a pagina de configuracoes de
    aparencia de video.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoDispAppearancePage : dword : 00000000 = Desabilitado;
    00000001 = Habilitada restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispAppearancePage"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\System]
"NoDispAppearancePage"=dword:00000000'''

# SECTION SECURITY
# SUB-SECTION CONTROL PANEL
# SUB-SECTION PRINTERS

def no_add_printer(on=0):
    
    """Desabilitar a Adicao de Impressoras
    
    DESCRIPTION
        Qualquer usuario pode adicionar uma nova impressora no seu sistema. 
    Esta opcao, quando habilitada, desabilita a adicao de novas impressoras no
    computador.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoAddPrinter : dword : 00000000 = Desabilitado;
    00000001 = Habilitada restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoAddPrinter"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoAddPrinter"=dword:00000000'''

def no_delete_printer(on=0):
    
    """Desabilitar a Exclusao de Impressoras
    
    DESCRIPTION
        Impressoras podem ser excluidas com o simples pressionar da tecla
    "delete". Habilitando este ajuste, usuarios nao serao mais capazes de
    excluir suas impressoras.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoDeletePrinter : dword : 00000000 = Desabilitado;
    00000001 = Habilitada restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoDeletePrinter"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoDeletePrinter"=dword:00000000'''

# SECTION SECURITY
# SUB-SECTION DESKTOP AND EXPLORER

def no_properties_recycle_bin(on=0):
    
    """Remover a Opcao Propriedades do Menu de Contexto da Lixeira
    
    DESCRIPTION
        Esta entrada lhe permite restringir o acesso a opcao Propriedades do 
    menu de contexto da Lixeira.
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        NoPropertiesRecycleBin : dword : 00000000 = Restricao desativada;
    00000001 = Restricao ativada.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoPropertiesRecycleBin"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoPropertiesRecycleBin"=dword:00000000'''

def no_properties_my_computer(on=0):
    
    """Remover a Opcao Propriedades do Menu de Contexto do "Meu Computador"
    
    DESCRIPTION
        Esta restricao remove a opcao Propriedades do "Meu Computador" e 
    esconde a tela "Propriedades do Sistema".
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED VALUES
        NoPropertiesMyComputer : dword : 00000000 = Restricao desativada;
    00000001 = Restricao ativada.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoPropertiesMyComputer"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoPropertiesMyComputer"=dword:00000000'''

def no_properties_my_documents(on=0):
    
    """Remover a Opcao Propriedades do Menu de Contexto do Diretorio
    "Meus Documentos"
    
    DESCRIPTION
        Esta entrada lhe permite remover a opcao Propriedades do menu de
    contexto do diretorio "Meus Documentos" (botao direito sobre o diretorio).
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED VALUES
        NoPropertiesMyDocuments : dword : 00000000 = Restricao desativada;
    00000001 = Restricao ativada.
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoPropertiesMyDocuments"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoPropertiesMyDocuments"=dword:00000000'''

def scr_sav_is_secure(on=0):
    
    """Politica de Protecao da Senha da Protecao de Tela
    
    DESCRIPTION
        Esta restricao determina se a protecao de tela e protegida por senha e
    previne que os usuarios alterem a configuracao de protecao por senha.
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        ScreenSaverIsSecure : dword : 00000000 = Protecoes de tela sem senha;
    00000001 = Protecoes de tela com senha.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\\
Control Panel\\Desktop]
"ScreenSaverIsSecure"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\\
Control Panel\\Desktop]
"ScreenSaverIsSecure"=dword:00000000'''

def enforce_shell_extension_security(on=0):
    
    """Forcar Seguranca nas Extensoes Shell
    
    DESCRIPTION
        Esta restricao pode ser usada para limitar o sistema a somente executar
    arquivos que tem uma extensao shell aprovada.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        EnforceShellExtensionSecurity : dword : 00000000 = Desabilitado;
    00000001 = Restricao habilitada.
    
    OBSERVATION
        As extensoes aprovadas estarao listadas na chave: [HKEY_LOCAL_MACHINE\
    Software\Microsoft\Windows\CurrentVersion\Shell Extensions\Approved]
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"EnforceShellExtensionSecurity"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"EnforceShellExtensionSecurity"=dword:00000000'''

def wallpaper_image_and_style(properties=[0, "C:\\Wallpaper.bmp", 0]):
    
    """Especificar a Imagem e o Estilo do Papel de Parede
    
    DESCRIPTION
        Estas configuracoes lhe permitem especificar a imagem de papel de 
    parede e o estilo de amostragem.
    
    COMPATIBILITY
        Windows 2000/Me/XP
    
    MODIFIED VALUES
        TileWallpaper : string : "0" = Mozaico habilitado; "1" = Desabilitado.
        Wallpaper : string : Recebe o caminho completo da imagem de papel de
    parede.
        WallpaperStyle : string : "0" = Centralizado; "1" = Lado a lado;
    "2" = Estendido.
    
    """
    return '''[HKEY_CURRENT_USER\\Control Panel\\Desktop]
"TileWallpaper"="%d"
"Wallpaper"="%s"
"WallpaperStyle"="%d"
''' %  (int(properties[0]), properties[1], int(properties[2]))

def no_security_tab(on=0):
    
    """Remover a Guia Seguranca
    
    DESCRIPTION
        Esta restricao remove a guia Seguranca do Windows Explorer, o que
    previne que os usuarios acessem ou alterem as permissoes de seguranca de
    diretorios e arquivos.
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED VALUES
        NoSecurityTab : dword : 00000000 = Desabilitado;
    00000001 = Restricao habilitada.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSecurityTab"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSecurityTab"=dword:00000000'''

def no_hardware_tab(on=0):
    
    """Remover a Guia Hardware
    
    DESCRIPTION
        Esta restricao remove a guia "Hardware" de itens aplicaveis no Painel 
    de Controle a das propriedades de drives locais. Isto previne a alteracao 
    das propriedades dos dispositivos pelos usuarios.
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        NoHardwareTab : dword : 00000000 = Desabilitado;
    00000001 = Restricao habilitada.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoHardwareTab"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoHardwareTab"=dword:00000000'''

def no_file_associate(on=0):
    
    """Remover a Habilidade de Modificar Tipos de Arquivos
    
    DESCRIPTION
        Esta configuracao lhe permite remover a habilidade de alterar, 
    adicionar ou remover tipos de arquivos usando a opcao "Opcoes de pasta" no 
    Windows Explorer.
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        NoFileAssociate : dword : 00000000 = Botoes habilitados;
    00000001 = Botoes desabilitados.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoFileAssociate"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoFileAssociate"=dword:00000000'''

# SECTION SECURITY
# SUB-SECTION LOGIN AND AUTHENTICATION

def disable_password_caching(on=0):
    
    """Desabilitar o Cache de Senhas no Internet Explorer
    
    DESCRIPTION
        Quando voce tenta visualizar um site protegido por senha, normalmente e
    pedido que se digite o nome de usuario e a senha, com uma opcao "Salvar 
    esta senha na sua lista de senhas". Esta entrada pode ser usada para 
    desabilitar esta habilidade de usuarios salvarem senhas.
    
    COMPATIBILITY
        Windows 2000/XP
    
    MODIFIED VALUES
        DisablePasswordCaching : dword : 00000000 = Padrao;
    00000001 = Desabilita a cache de senhas.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Internet Settings]
"DisablePasswordCaching"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Internet Settings]
"DisablePasswordCaching"=dword:00000000'''

def alphanum_passwords(on=0):
    
    """Requerer Senha Alfanumerica para o Windows
    
    DESCRIPTION
        O Windows, por padrao, aceitara qualquer senha como valida, inclusive o
    valor nulo. Esta configuracao controla se o Windows ira requerer uma senha
    alfanumerica, i.e. uma senha feita da combinacao de caracteres alfa(A, B, 
    C,...) e numericos (1, 2, 3, ...).
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        AlphanumPwds : dword : 00000000 = Desabilita o recurso;
    00000001 = Habilita.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Network]
"AlphanumPwds"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Network]
"AlphanumPwds"=dword:00000000'''

# SECTION SECURITY
# SUB-SECTION NETWORK

def no_net_connect_disconnect(on=0):
    
    """Remover a Opcao Mapear Unidade de Rede
    
    DESCRIPTION
        Previne que usuarios facam configuracoes adicionais a partir da opcao
    Mapear Unidade de Rede. Isto removera a opcao Mapear Unidade de Rede da
    barra de ferramentas do Windows Explorer e o do menu de contexto do "Meu
    Computador".
    
    COMPATIBILITY
        Windows 2000/Me/XP
    
    MODIFIED VALUES
        NoNetConnectDisconnect : dword : 00000000 = Restricao desabilitada;
    00000001 = Habilita restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoNetConnectDisconnect"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoNetConnectDisconnect"=dword:00000000'''

# SECTION SECURITY
# SUB-SECTION START MENU AND TASKBAR

def no_change_start_menu(on=0):
    
    """Desabilitar o "Drag-and-Drop" no Menu Iniciar
    
    DESCRIPTION
        Esta restricao previne que os usuarios modifiquem o menu Iniciar,
    atraves do recurso "Drag-and-Drop".
    
    COMPATIBILITY
        Windows 98/Me/2000/XP
    
    MODIFIED VALUES
        NoChangeStartMenu : dword : 00000000 = Desabilita restricao;
    00000001 = Habilita restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoChangeStartMenu"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoChangeStartMenu"=dword:00000000'''

def no_run(on=0):
    
    """Excluir a Opcao Executar do Menu Iniciar
    
    DESCRIPTION
        Remove a capacidade de executar comandos ou processos da menu iniciar
    excluindo a opcao Executar.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoRun : dword : 00000000 = Desabilitado; 00000001 = Habilita restricao.
        
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoRun"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoRun"=dword:00000000'''

def no_set_task_bar(on=0):
    
    """Esconder o Icone Barra de Tarefas e Menu Iniciar
    
    DESCRIPTION
        Esta restricao remove o icone Barra de Tarefas e Menu Iniciar do Painel
    de Controle e o item Propriedades do menu de contexto do menu Iniciar.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoSetTaskbar : dword : 00000000 = Desabilitado;
    00000001 = Habilita restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSetTaskbar"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSetTaskbar"=dword:00000000'''

# SECTION SECURITY
# SUB-SECTION START MENU AND TASKBAR
# SUB-SECTION DOCUMENTS AND FOLDER

def no_recent_docs_history(on=0):
    
    """Desabilitar Historico de Documentos Recentes
    
    DESCRIPTION
        Normalmente quando voce abre um arquivo, isso e adicionado a lista de
    documentos recentes no menu Iniciar. Esta entrada fara com que novos
    arquivos nao sejam adicionados nesta lista.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoRecentDocsHistory : dword : 00000000 = Desabilitado;
    00000001 = Remove opcao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoRecentDocsHistory"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoRecentDocsHistory"=dword:00000000'''

def no_start_menu_music(on=0):
    
    """Remove a Opcao "Minhas Musicas" do Menu Iniciar
    
    DESCRIPTION
        Esta restricao remove a opcao "Minhas Musicas" do menu iniciar.
    
    COMPATIBILITY
        Windows 2000/Me/XP
    
    MODIFIED VALUES
        NoStartMenuMyMusic : dword : 00000000 = Desabilitado;
    00000001 = Remove opcao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoStartMenuMyMusic"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoStartMenuMyMusic"=dword:00000000'''

def no_show_menu_my_pics(on=0):
    
    """Remove a Opcao "Minhas Imagens" do Menu Iniciar
    
    DESCRIPTION
        Esta restricao remove a opcao "Minhas Imagens" do menu iniciar.
    
    COMPATIBILITY
        Windows 2000/Me/XP
    
    MODIFIED VALUES
        NoSMMyPictures : dword : 00000000 = Desabilitado;
    00000001 = Remove opcao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSMMyPictures"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSMMyPictures"=dword:00000000'''

def no_faves_menu(on=0):
    
    """Remove a Opcao "Favoritos" do Menu Iniciar
    
    DESCRIPTION
        Esta restricao remove a opcao "Favoritos" do menu iniciar.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoFavoritesMenu : dword : 00000000 = Desabilitado;
    00000001 = Remove opcao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoFavoritesMenu"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoFavoritesMenu"=dword:00000001'''

# SECTION WINDOWS

def change_special_dirs_path(parameters=["Meus Documentos", "C:\\Meus Documentos"]):
    
    """Alterar a Localizacao do Sistema e Diretorios Especiais
    
    DESCRIPTION
        O Windows possui alguns diretorios especiais como "Meu Computador",
    "Area de Trabalho", "Favoritos" e "Menu Iniciar". Esses diretorios podem
    ser movidos para qualquer lugar no sistema e a nova localizacao atualizada
    nesta chave.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        AppData : Dados de aplicativos
        Cache : Arquivos temporarios de Internet
        Cookies : Diretorio de armazenagem de Cookies
        Desktop : Area de trabalho
        Favorites : Diretorio de favoritos
        History : Diretorio de historicos
        Local Appdata : Dados locais de aplicativos
        Local Settings : Configuracoes locais
        My Pictures : Minhas imagens
        NetHood : Ambiente de rede
        Personal : Meus documentos
        PrintHood : Ambiente de impressao
        Programs : Programas do menu iniciar
        Recent : Documentos recentes
        SendTo : Enviar para
        Start Menu : Menu iniciar
        Startup : Inicializar
        Templates : Modelos
    
    OBSERVATION
        Todos os valores descritos acima, por trabalharem com variaveis do
    sistema, sao do tipo REG_EXPAND_SZ. Isso significa que os valores devem ser
    atribuidos a eles de uma forma diferente (como se pode ver abaixo). E'
    aconselhavel utilizar um editor hexadecimal ou um script que converta uma
    string para o formato utilizado por este tipo de valor.
    
    """
    
    def translate(strn=''):
        
        """Converte cada caractere da string passada como parâmetro para sua
        representação em hexadecimal.
        
        """
        
        ret = []
        
        for s in strn : ret.append("%02X" % ord(s))
        
        return ret
    
    def re4(lst=[]):
        
        """Retorna uma string no formato esperado pela versao 4 do editor do
        registro do Windows.
        
        """
        
        ret = []
        
        for l in lst : ret.append(l + ",")
        else: ret.append("00")
        
        return ret
    
    def re5(lst):
        
        """Retorna uma string no formato esperado pela versao 5 do editor do
        registro do Windows.
        
        """
        
        ret = []
        
        for l in lst: ret.append(l + ",00,")
        else: ret.append("00,00")
        
        return ret
    
    def printer(stn, lst, sum):
        
        """Retorna a saida do programa pronta para ser impressa na tela."""
        
        lBreak = len( stn ) + 9
        ret = '"' + stn + '"=hex(2):'
        
        for l in lst:
            if (lBreak <= (79 - sum)):
                ret += l
                lBreak += sum
            
            else:
                lBreak = 0
                ret += l + '\\\n'
        
        else:
            if (ret[len(ret) - 2] == '\\'):
                ret = ret[0:len(ret) - 2]
        
        return ret
    
    return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Explorer\\User Shell Folders]
%s
''' % (printer(parameters[0], re4(translate(parameters[1])), 4))
# ...re5(translate(parameters[1])), 7))

# SECTION SECURITY
# SUB-SECTION SYSTEM

def prompt_password_on_resume(on=0):
    
    """Pedir Senha ao Resumir
    
    DESCRIPTION
        Este ajuste lhe permite configurar o computador para sempre travar e
    requerer uma senha apos voltar da hibernacao ou modo suspenso.
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED VALUES
        PromptPasswordOnResume : dword : 00000000 = Sem pedir senha;
    00000001 = Pede a senha.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\\
System\\Power]
"PromptPasswordOnResume"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\\
System\\Power]
"PromptPasswordOnResume"=dword:00000000'''

# SECTION SOFTWARE
# SUB-SECTION INTERNET EXPLORER
# SUB-SECTION SECURITY

def ie_restrictions(on=0):
    
    """Restricoes do Internet Explorer
    
    DESCRIPTION
        Estas entradas lhe permitem controlar o acesso as configuracoes do
    Internet Explorer e funcoes do Painel de Controle (encontrados em
    Ferramentas/Opcoes de Internet).
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        Accessibility : Desabilita todas as opcoes de acebilidade.
        Advanced : Previne alteracoes nas configuracoes avancadas.
        AdvancedTab : Remove a guia Avancado.
        Autoconfig : Previne alteracoes nas configuracoes automaticas.
        Cache : Previne alteracoes nas configuracoes de arquivos temporarios.
        CalendarContact : Previne alteracoes nos calendarios e contatos.
        Certificates : Previne alteracoes nos certificados de seguranca.
        CertifPers : Previne alteracoes nas opcoes de certificados pessoais.
        CertifPub : Previne alteracoes nas opcoes de certificados publicos.
        CertifSite : Previne alteracoes nas opcoes de certificados de sites.
        Check_If_Default : Previne alteracoes nas opcoes de browser padrao.
        Colors : Previne alteracoes nas cores.
        ConnectionsTab : Remove a guia Conexoes.
        Connwiz Admin Lock : Desabilita o assistente de conexao a Internet.
        Connection Settings : Previne alteracoes nas configuracoes de conexao.
        Connection Wizard : Desabilita o assistente de conexao.
        ContentTab : Remove a guia Conteudo.
        Fonts : Desabilita alteracoes na fonte.
        FormSuggest : Desabilita o "Auto-Completar" nos formularios.
        FormSuggest Passwords : Previne que a opcao de salvar senha seja
    mostrada.
        GeneralTab : Remove a guia Geral.
        History : Desabilita alteracoes na configuracao do historico.
        HomePage : Desabilita alteracoes nas configuracoes de pagina inicial.
        Languages : Desabilita alteracoes na linguagem.
        Links : Desabilita alteracoes nos links.
        Messaging : Desabilita alteracoes nas mensagens.
        PrivacyTab : Remove a guia Privacidade.
        Privacy Settings : Previne alteracoes nas configuracoes de privacidade.
        Profiles : Desabilita alteracoes nos perfis.
        ProgramsTab : Remove a guia Programas.
        Proxy : Desabilita alteracoes nas configuracoes de proxy.
        Ratings : Desabilita alteracoes nas avaliacoes.
        ResetWebSettings : Desabilita o botao de reconfiguracao das
    configuracoes de Internet.
        SecAddSites : Previne a adicao de sites em qualquer zona.
        SecChangeSettings : Previne alteracoes nos niveis de seguranca para a
    zona de Internet.
        SecurityTab : Remove a guia Seguranca.
        Settings : Previne quaisquer alteracoes nos arquivos temporarios.
        Wallet : Desabilita alteracoes nas configuracoes de carteira.
    
    OBSERVATION
        Todos os valores modificados sao do tipo dword. Para todos eles, o 
    valor 00000000 desabilita a opcao e o valor 00000001 habilita.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\\
Internet Explorer\\Control Panel]
"Accessibility"=dword:00000001
"Advanced"=dword:00000001
"AdvancedTab"=dword:00000001
"Autoconfig"=dword:00000001
"Cache"=dword:00000001
"CalendarContact"=dword:00000001
"Certificates"=dword:00000001
"CertifPers"=dword:00000001
"CertifPub"=dword:00000001
"CertifSite"=dword:00000001
"Check_If_Default"=dword:00000001
"Colors"=dword:00000001
"ConnectionsTab"=dword:00000001
"Connwiz Admin Lock"=dword:00000001
"Connection Settings"=dword:00000001
"Connection Wizard"=dword:00000001
"Fonts"=dword:00000001
"FormSuggest"=dword:00000001
"FormSuggest Passwords"=dword:00000001
"GeneralTab"=dword:00000001
"History"=dword:00000001
"HomePage"=dword:00000001
"Languages"=dword:00000001
"Links"=dword:00000001
"Messaging"=dword:00000001
"PrivacyTab"=dword:00000001
"Privacy Settings"=dword:00000001
"Profiles"=dword:00000001
"ProgramsTab"=dword:00000001
"Proxy"=dword:00000001
"Ratings"=dword:00000001
"ResetWebSettings"=dword:00000001
"SecAddSites"=dword:00000001
"SecChangeSettings"=dword:00000001
"SecurityTab"=dword:00000001
"Settings"=dword:00000001
"Wallet"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\\
Internet Explorer\\Control Panel]
"Accessibility"=dword:00000000
"Advanced"=dword:00000000
"AdvancedTab"=dword:0000000
"Autoconfig"=dword:00000000
"Cache"=dword:00000000
"CalendarContact"=dword:00000000
"Certificates"=dword:00000000
"CertifPers"=dword:00000000
"CertifPub"=dword:00000000
"CertifSite"=dword:00000000
"Check_If_Default"=dword:0000000
"Colors"=dword:00000000
"ConnectionsTab"=dword:00000000
"Connwiz Admin Lock"=dword:00000000
"Connection Settings"=dword:00000000
"Connection Wizard"=dword:00000000
"Fonts"=dword:00000000
"FormSuggest"=dword:00000000
"FormSuggest Passwords"=dword:00000000
"GeneralTab"=dword:00000000
"History"=dword:00000000
"HomePage"=dword:00000000
"Languages"=dword:00000000
"Links"=dword:00000000
"Messaging"=dword:00000000
"PrivacyTab"=dword:00000000
"Privacy Settings"=dword:00000000
"Profiles"=dword:00000000
"ProgramsTab"=dword:00000000
"Proxy"=dword:00000000
"Ratings"=dword:00000000
"ResetWebSettings"=dword:00000000
"SecAddSites"=dword:00000000
"SecChangeSettings"=dword:00000000
"SecurityTab"=dword:00000000
"Settings"=dword:00000000
"Wallet"=dword:00000000'''

# SECTION WINDOWS
# SUB-SECTION DESKTOP

def no_desktop_cleanup_wizard(on=0):
    
    """Desabilitar o Assistente de Limpeza do Desktop
    
    DESCRIPTION
        Esta restricao desabilita o Assistente de Limpeza do Desktop, um
    software que verifica periodicamente se ha icones que nao sao usados na 
    area de trabalho.
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED VALUES
        NoDesktopCleanupWizard : dword : 00000000 = Desabilitado;
    00000001 = Habilita restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoDesktopCleanupWizard"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoDesktopCleanupWizard"=dword:00000000'''

def no_internet_icon(on=0):
    
    """Esconder o Icone do Internet Explorer do Desktop
    
    DESCRIPTION
        Esta entrada esconde o icone do Internet Explorer do Desktop do 
    Windows.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoInternetIcon : dword : 00000000 = Desativado;
    00000001 = Remove o icone.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoInternetIcon"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoInternetIcon"=dword:00000000'''

def no_view_context_menu(on=0):
    
    """Desabilitar a Habilidade de Clicar com o Botao Direito no Desktop
    
    DESCRIPTION
        Esta entrada remove o menu de contexto que normalmente apareceria 
    quando o usuario clica com o botao direito do mouse no Desktop ou no painel
    da\ direita do Windows Explorer.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoViewContextMenu : dword : 00000000 = Desativado;
    00000001 = Remove o menu.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoViewContextMenu"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoViewContextMenu"=dword:00000000'''

# SECTION WINDOWS
# SUB-SECTION ACCESSORIES
# SUB-SECTION REGISTRY EDITOR

def cancel_registry_imports(on=0):
    
    """Anular Importacoes Acidentais no Registro
    
    DESCRIPTION
        Por padrao, se voce der um duplo clique sobre um arquivo com a extensao
    ".reg", o arquivo sera importado pelo registro do sistema. Se voce alterar 
    o padrao, o arquivo sera aberto para edicao em vez de ser importado.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        @ : string : "edit" = ativa a funcao.
        
    """
    
    if on:
        return '''[HKEY_CLASSES_ROOT\\regfile\\shell]
@="edit"'''
    
    else:
        return '''[HKEY_CLASSES_ROOT\\regfile\\shell]
@=-'''

# SECTION WINDOWS
# SUB-SECTION LOGIN AND AUTHENTICATION

def logon_wallpaper_and_style(parameters=[0, "C:\\Wallpaper.bmp", 0]):
    
    """Alterar o Papel de Parede da Tela de Logon
    
    DESCRIPTION
        Quando voce configura um papel de parede para o seu desktop, a tela
    inicial de logon nao e alterada e permanece com a aparencia padrao do
    Windows. Esta entrada lhe permite alterar o papel de parede padrao.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        TileWallpaper : string : "0" = Mozaico habilitado; "1" = Desabilitado.
        Wallpaper : string : Contem o caminho do papel de parede (BMP).
        WallpaperStyle : string : "0" = Centralizado; "1" = Lado a lado;
    "2" = Estendido.
    
    """
    
    return '''[HKEY_USERS\\.DEFAULT\\Control Panel\\Desktop]
"TileWallpaper"="%d"
"Wallpaper"="%s"
"WallpaperStyle"="%d"
''' % (int(parameters[0]), parameters[1], int(parameters[2]))

# SECTION WINDOWS
# SUB-SECTION START MENU AND TASKBAR
# SUB-SECTION TASKBAR

def no_tray_context_menu(on=0):
    
    """Desabilitar Menu de Contexto na Barra de Tarefas
    
    DESCRIPTION
        Esta configuracao remove o menu de contexto (botao direito na barra de
    tarefas).
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoTrayContextMenu : dword : 00000000 = Desabilitado;
    00000001 = Habilita restricao.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoTrayContextMenu"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoTrayContextMenu"=dword:00000000'''

def enable_auto_tray(on=0):
    
    """Esconder Automaticamente Icones Inativos na Bandeja
    
    DESCRIPTION
        Este ajuste controla se programas executando na bandeja devem ser
    escondidos automaticamente quando estao inativos.
    
    COMPATIBILITY
        Windows XP
    
    MODIFIED VALUES
        EnableAutoTray : dword : 00000000 = Mostra icones inativos;
    00000001 = Esconde icones inativos.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Explorer]
"EnableAutoTray"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Explorer]
"EnableAutoTray"=dword:00000000'''

# SECTION WINDOWS
# SUB-SECTION STARTUP AND SHUTDOWN

def no_save_settings(on=0):
    
    """Desabilitar Salvamento de Configuracoes ao Sair
    
    DESCRIPTION
        Quando o Windows e desligado, ele normalmente salva o layout do 
    Desktop, incluindo a localizacao dos icones, aparencia e outros parametros.
    Este ajuste descarta quaisquer alteracoes feitas anteriormente, preservando
    o layout configurado.
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        NoSaveSettings : dword : 00000000 = Desabilitado;
    00000001 = Restricao habilitada.
    
    """
    
    if on:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSaveSettings"=dword:00000001'''
    
    else:
        return '''[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\\
CurrentVersion\\Policies\\Explorer]
"NoSaveSettings"=dword:00000000'''

# SECTION WINDOWS
# SUB-SECTION WINDOWS EXPLORER

def show_copy_move_send(on=0):
    
    """Adicionar as Opcoes Copiar, Mover e Enviar Para
    
    DESCRIPTION
        Esta entrada lhe permite copiar e mover facilmente arquivos e 
    diretorios com o simples clique do botao direito do mouse e com a selecao 
    posterior da opcao "Copiar Para", "Mover Para" ou "Enviar Para".
    
    COMPATIBILITY
        Todos.
    
    MODIFIED VALUES
        @ : string :
    "{C2FBB630-2971-11d1-A18C-00C04FD75D13}" = adiciona a opcao "Copiar Para".
        @ : string :
    "{C2FBB631-2971-11d1-A18C-00C04FD75D13}" = adiciona a opcao "Mover Para".
        @ : string :
    "{7BA4C740-9E81-11CF-99D3-00AA004AE837}" = adiciona a opcao "Enviar Para".
    
    OBSERVATION
        Basta atribuir um valor nulo para qualquer uma das três chaves, para
    inibir a sua exibicao (e.g., @="").
    
    """
    
    if on:
        return '''[HKEY_CLASSES_ROOT\\AllFilesystemObjects\\shellex\\\
ContextMenuHandlers\\Copy To]
@="{C2FBB630-2971-11d1-A18C-00C04FD75D13}"

[HKEY_CLASSES_ROOT\\AllFilesystemObjects\\shellex\\ContextMenuHandlers\\\
Move To]
@="{C2FBB631-2971-11d1-A18C-00C04FD75D13}"

[HKEY_CLASSES_ROOT\\AllFilesystemObjects\\shellex\\ContextMenuHandlers\\\
Send To]
@="{7BA4C740-9E81-11CF-99D3-00AA004AE837}"'''
    
    else:
        return '''[HKEY_CLASSES_ROOT\\AllFilesystemObjects\\shellex\\\
ContextMenuHandlers\\Copy To]
@=""

[HKEY_CLASSES_ROOT\\AllFilesystemObjects\\shellex\\ContextMenuHandlers\\\
Move To]
@=""

[HKEY_CLASSES_ROOT\\AllFilesystemObjects\\shellex\\ContextMenuHandlers\\\
Send To]
@=""'''


# TODO: Make a graphic interface to WRF. 
#       Translate all function docstrings to English.
