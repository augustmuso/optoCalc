from core.py_optometry_formulae import OptometryFormulas
from core.ret_arth import RefractionPrescription

def main():
    # Example usage of OptometryFormulas class
    distance = 2.5
    power = -3.0
    prentice_result = OptometryFormulas.prentice(distance, power)
    print("Prentice formula result:", prentice_result)

    # Example usage of RefractionPrescription class
    kaw_old = RefractionPrescription(Px='-3.00/-1.00X15')
    kaw_new = RefractionPrescription(Px='-3.25/-1.00X15')
    x = kaw_new - kaw_old
    print("Prescription change:", x.Px)

    # You can continue using other formulas as needed


if __name__ == "__main__":
    main()