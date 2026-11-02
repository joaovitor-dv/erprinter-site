# Site público do ERPrinter

Página inicial, termos de uso e política de privacidade do ERPrinter, para hospedar no GitHub Pages com o domínio `erprinter.com`. Serve como Website URL do app na Etsy e reúne os textos obrigatórios da Etsy (aviso de marca e e-mail de suporte).

## Estrutura

- `src/index.html`: conteúdo da página inicial.
- `src/terms.md` e `src/privacy.md`: textos legais, gerados a partir dos rascunhos em `erp-adaptavel/docs/etsy/`.
- `build.py`: monta `index.html`, `terms.html` e `privacy.html` com cabeçalho, rodapé e aviso de rascunho.
- `style.css`, `CNAME` (`erprinter.com`) e `.nojekyll` (publica os arquivos como estão).

Para regenerar as páginas depois de editar `src/`:

```bash
python3 build.py
```

## Antes de publicar

1. **Domínio:** comprar `erprinter.com` (decisão do João em 2026-11-02).
2. **E-mail:** criar `support@`, `security@` e `privacy@erprinter.com`. O GitHub Pages não recebe e-mail; é preciso redirecionamento no registrador ou um serviço de e-mail.
3. **Textos legais:** os termos e a política estão como rascunho, com aviso na página. Faltam entidade jurídica, endereço, cláusulas jurídicas e prazos de retenção ([*]). Precisam de revisão de advogado.
4. **Publicação:** criar um repositório **público** separado no GitHub, enviar estes arquivos, ativar o Pages pela branch `main` e configurar o DNS do domínio. Cada passo exige autorização do João.

## Estado

Preparado em 2026-11-02 por ERP_ADP_CLAUDE_DEV e publicado no GitHub Pages com autorização do João no mesmo dia. Os textos legais seguem como rascunho.
