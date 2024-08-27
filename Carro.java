public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private String cor;
    private double preco;

    public Carro(String marca, String modelo, int ano, String cor, double preco) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.cor = cor;
        this.preco = preco;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String novaMarca) {
        this.marca = novaMarca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String novoModelo) {
        this.modelo = novoModelo;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int novoAno) {
        this.ano = novoAno;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String novaCor) {
        this.cor = novaCor;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double novoPreco) {
        this.preco = novoPreco;
    }

    public static void main(String[] args) {
        Carro meuCarro = new Carro("Toyota", "Corolla", 2020, "Preto", 50000);

        // Obtendo os valores dos atributos
        System.out.println("Marca: " + meuCarro.getMarca());
        System.out.println("Modelo: " + meuCarro.getModelo());
        System.out.println("Ano: " + meuCarro.getAno());
        System.out.println("Cor: " + meuCarro.getCor());
        System.out.println("Preço: " + meuCarro.getPreco());

        // Alterando valores dos atributos
        meuCarro.setModelo("Camry");
        meuCarro.setAno(2021);
        meuCarro.setCor("Branco");
        meuCarro.setPreco(55000);

        // Verificando as alterações
        System.out.println("Novo modelo: " + meuCarro.getModelo());
        System.out.println("Novo ano: " + meuCarro.getAno());
        System.out.println("Nova cor: " + meuCarro.getCor());
        System.out.println("Novo preço: " + meuCarro.getPreco());
    }
}
