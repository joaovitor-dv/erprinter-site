# DNS e e-mail de erprinter.com

Domínio registrado pelo João na Cloudflare em 2026-11-02. Os nameservers `sid.ns.cloudflare.com` e `walk.ns.cloudflare.com` foram conferidos com `dig` no mesmo dia. Nenhum valor secreto fica neste arquivo.

Siga a ordem abaixo. Verificar o domínio no GitHub **antes** de apontar o DNS impede que outra conta do GitHub tome o domínio.

## 1. Verificar o domínio no GitHub

1. GitHub → foto do perfil → **Settings → Pages → Add a domain** → `erprinter.com`.
2. O GitHub mostra um registro TXT. Crie-o na Cloudflare (**DNS → Records → Add record**):

| Tipo | Nome | Conteúdo | Proxy |
| --- | --- | --- | --- |
| TXT | `_github-pages-challenge-joaovitor-dv` | valor exibido pelo GitHub | — |

3. Volte ao GitHub e clique em **Verify**. A propagação pode levar alguns minutos.

## 2. E-mail (Cloudflare Email Routing)

1. Cloudflare → `erprinter.com` → **Email → Email Routing → Get started**. A Cloudflare cria sozinha os registros MX e o TXT de SPF; aceite a sugestão.
2. Em **Destination addresses**, cadastre a caixa pessoal que você vai monitorar e confirme pelo link que chega nela.
3. Em **Custom addresses**, crie três endereços com destino nessa caixa:

| Endereço | Uso |
| --- | --- |
| `support@erprinter.com` | Suporte aos sellers (obrigatório pela Etsy) |
| `security@erprinter.com` | Incidentes de segurança |
| `privacy@erprinter.com` | Pedidos de privacidade |

O Email Routing só **recebe**. Para responder com o endereço `@erprinter.com`, é preciso configurar envio à parte (Gmail "enviar como" com um serviço SMTP, por exemplo). Enquanto isso não existir, responda pela caixa pessoal.

## 3. Apontar o site para o GitHub Pages

Só depois de criar o repositório público e ativar o Pages com o domínio `erprinter.com`. Proxy **desligado** (nuvem cinza, "DNS only"), para o GitHub conseguir emitir o certificado HTTPS.

| Tipo | Nome | Conteúdo |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |
| CNAME | `www` | `joaovitor-dv.github.io` |

Depois que o DNS propagar, marque **Enforce HTTPS** nas configurações do Pages do repositório.

## Conferência

```bash
dig +short A erprinter.com
```

```bash
dig +short MX erprinter.com
```
