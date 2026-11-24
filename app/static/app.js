// RESPONSABLE: Integrante 5  RAMA: feature/frontend

const $ = (id) => document.getElementById(id);

const ENCENDIDOS = new Set(["ENCENDIDO", "ACTIVADA", "ABIERTA"]);

function pintarDispositivos(lista) {
  $("dispositivos").innerHTML = lista
    .map(
      (d) => `
      <div class="dispositivo ${ENCENDIDOS.has(d.estado) ? "on" : ""}">
        <span class="foco"></span>
        <strong>${d.id}</strong>
        <small>${d.tipo}</small>
        <span class="estado">${d.estado}</span>
      </div>`
    )
    .join("");
}

function pintarSalida(r) {
  $("tokens").textContent = r.tokens.map((t) => `${t.tipo.padEnd(14)} ${t.lexema}`).join("\n");
  $("ast").textContent = r.ast ? JSON.stringify(r.ast, null, 2) : "";
  $("ir").textContent = r.ir.join("\n");
  $("ir-opt").textContent =
    r.ir_optimizado.join("\n") + (r.optimizaciones.length ? "\n\n# " + r.optimizaciones.join("\n# ") : "");

  $("errores").innerHTML = r.errores
    .map((e) => `<p class="error">Error ${e.fase}${e.linea ? ` (línea ${e.linea})` : ""}: ${e.mensaje}</p>`)
    .join("");
  $("resultados").innerHTML = r.resultados.map((x) => `<p class="ok">${x.mensaje}</p>`).join("");
}

async function enviar(ejecutar) {
  const resp = await fetch("/api/ejecutar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ codigo: $("codigo").value, ejecutar }),
  });
  const r = await resp.json();
  pintarSalida(r);
  pintarDispositivos(r.dispositivos);
}

async function cargarDispositivos() {
  const resp = await fetch("/api/dispositivos");
  pintarDispositivos(await resp.json());
}

$("btn-ejecutar").addEventListener("click", () => enviar(true));
$("btn-analizar").addEventListener("click", () => enviar(false));
$("btn-reiniciar").addEventListener("click", async () => {
  await fetch("/api/reiniciar", { method: "POST" });
  cargarDispositivos();
});
$("codigo").addEventListener("keydown", (e) => {
  if (e.key === "Enter" && e.ctrlKey) enviar(true);
});

cargarDispositivos();
